#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============================================================================
 EMPIRE DESK  —  System Tray Command Center (PySide6)  —  v3 (Production)
============================================================================
Launcher minimalista per Windows nella System Tray per gli script di
automazione. v3 aggiunge: auto-reload della config, limite di esecuzioni
concorrenti + coda, e icona animata (spinner) quando girano workflow.

Tutto PySide6 puro (nessuna libreria esterna extra).

----------------------------------------------------------------------------
 ESEMPIO DI workflows.json:

 {
   "settings": {
     "log_file":      "empire_desk.log",  // "" o omesso -> nessun log
     "python":        "auto",             // "auto" = sys.executable
     "auto_reload":   true,               // ricarica su modifica file
     "max_concurrent": 2                  // max workflow paralleli
   },
   "workflows": [
     {
       "name": "Pulizia Log",
       "script_path": "scripts/clean_logs.py",
       "args": ["--verbose"],   // opzionale
       "cwd":  "scripts",       // opzionale (relativo allo script)
       "enabled": true          // opzionale (default true)
     }
   ]
 }
----------------------------------------------------------------------------
"""

import sys
import json
import logging
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
    QSystemTrayIcon,
    QMenu,
    QMessageBox,
    QInputDialog,
    QDialog,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
)
from PySide6.QtGui import (
    QIcon,
    QAction,
    QPixmap,
    QPainter,
    QColor,
    QFont,
    QPen,
    QDesktopServices,
)
from PySide6.QtCore import (
    Qt,
    QProcess,
    QUrl,
    QTimer,
    QFileSystemWatcher,
    Signal,
    QObject,
    Slot,
    QThread,
)

LOGGER = logging.getLogger("EmpireDesk")


# ===========================================================================
#  WORKFLOW RUNNER
# ===========================================================================
class WorkflowRunner(QObject):
    """Esegue gli script via QProcess (non bloccante) con stop e tracing."""

    workflow_finished = Signal(str, bool, str)

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self._proc_by_name: dict[str, QProcess] = {}
        self._python = sys.executable

    def configure(self, python: str) -> None:
        self._python = python if python and python != "auto" else sys.executable

    def run(self, workflow: dict) -> None:
        name = workflow.get("name", "<senza nome>")
        script = workflow.get("script_path", "")
        args = workflow.get("args") or []
        cwd = workflow.get("cwd")

        script_path = Path(script)
        if not script_path.is_file():
            self.workflow_finished.emit(name, False, f"Script non trovato: {script}")
            return
        if name in self._proc_by_name:
            self.workflow_finished.emit(name, False, "Già in esecuzione.")
            return

        proc = QProcess(self)
        proc.setProgram(self._python)
        proc.setArguments([str(script_path)] + [str(a) for a in args])

        base = Path(__file__).resolve().parent
        workdir = (base / cwd) if cwd else script_path.parent
        proc.setWorkingDirectory(str(workdir))
        proc.setProcessChannelMode(QProcess.MergedChannels)

        if sys.platform.startswith("win"):
            try:
                proc.setCreateProcessArgumentsModifier(
                    lambda m: m.setFlag(QProcess.CreateProcessNoWindow, True)
                )
            except Exception:
                pass

        proc._already_notified = False  # type: ignore[attr-defined]
        proc._killed = False            # type: ignore[attr-defined]
        self._proc_by_name[name] = proc

        proc.finished.connect(
            lambda code, status, p=proc, n=name: self._on_finished(p, n, code, status)
        )
        proc.errorOccurred.connect(
            lambda err, p=proc, n=name: self._on_error(p, n, err)
        )
        proc.start()

    def stop(self, name: str) -> None:
        proc = self._proc_by_name.get(name)
        if proc and proc.state() != QProcess.NotRunning:
            proc._killed = True  # type: ignore[attr-defined]
            proc.kill()

    def _on_finished(self, proc: QProcess, name: str,
                     exit_code: int, exit_status: QProcess.ExitStatus) -> None:
        if proc._already_notified:  # type: ignore[attr-defined]
            return
        proc._already_notified = True  # type: ignore[attr-defined]
        self._proc_by_name.pop(name, None)

        if proc._killed:  # type: ignore[attr-defined]
            self.workflow_finished.emit(name, False, "Interrotto dall'utente.")
            self._cleanup(proc)
            return

        success = (exit_status == QProcess.NormalExit and exit_code == 0)
        raw = bytes(proc.readAllStandardOutput()).decode(errors="replace").strip()
        detail = (raw[-180:] if raw else f"Exit code: {exit_code}")
        self.workflow_finished.emit(name, success, detail)
        self._cleanup(proc)

    def _on_error(self, proc: QProcess, name: str,
                  error: QProcess.ProcessError) -> None:
        if proc._already_notified:  # type: ignore[attr-defined]
            return
        proc._already_notified = True  # type: ignore[attr-defined]
        self._proc_by_name.pop(name, None)
        self.workflow_finished.emit(name, False, proc.errorString())
        self._cleanup(proc)

    def _cleanup(self, proc: QProcess) -> None:
        proc.deleteLater()

    def terminate_all(self) -> None:
        for proc in list(self._proc_by_name.values()):
            if proc.state() != QProcess.NotRunning:
                proc.kill()
        self._proc_by_name.clear()


# ===========================================================================
#  APEX-7 WORKER  —  esegue l'Orchestrator in un thread separato
#  (così la tray non si blocca mentre APEX-7 "pensa").
# ===========================================================================
class ApexWorker(QThread):
    result_ready = Signal(str, str)   # draft, analysis
    error_occurred = Signal(str)

    def __init__(self, goal: str, db_path: str, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self.goal = goal
        self.db_path = db_path

    def run(self) -> None:
        try:
            # Import lazy: apex7 è opzionale rispetto a PySide6.
            from empire.intelligence.apex7.memory import MemoryEcosystem
            from empire.intelligence.apex7.orchestrator import Orchestrator
            mem = MemoryEcosystem(self.db_path)
            out = Orchestrator(memory=mem).run(self.goal)
            mem.close()
            self.result_ready.emit(out.get("draft", ""), out.get("analysis", ""))
        except Exception as exc:  # noqa: BLE001
            self.error_occurred.emit(str(exc))


# ===========================================================================
#  EMPIRE DESK  —  Controller UI / Tray / Menu
# ===========================================================================
class EmpireDesk(QSystemTrayIcon):
    CONFIG_FILE = "workflows.json"

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

        self.workflows: list[dict] = []
        self._dynamic_actions: list[QAction] = []
        self._name_to_action: dict[str, QAction] = {}
        self._running_names: set[str] = set()
        self._queue: list[dict] = []
        self._log_file: str | None = None
        self._max_concurrent: int = 4
        self._auto_reload: bool = True
        self._config_path: str = ""

        self.runner = WorkflowRunner(self)
        self.runner.workflow_finished.connect(self._on_workflow_finished)

        # Icona statica + frames animati + timer spinner.
        self._static_icon = self._build_static_icon()
        self._frames = self._build_spinner_frames()
        self._frame_idx = 0
        self._spin_timer = QTimer(self)
        self._spin_timer.setInterval(120)
        self._spin_timer.timeout.connect(self._next_frame)

        # Watcher per auto-reload della config.
        self._watcher = QFileSystemWatcher(self)
        self._watcher.fileChanged.connect(self._on_config_changed)

        self._build_base_menu()
        self.setIcon(self._static_icon)
        self.load_workflows()
        self.populate_workflows()

        self._update_tooltip()
        self.setVisible(True)

        QApplication.instance().aboutToQuit.connect(self.runner.terminate_all)

    # ------------------------------------------------------------------
    #  ICONE
    # ------------------------------------------------------------------
    def _build_static_icon(self) -> QIcon:
        pix = QPixmap(32, 32)
        pix.fill(Qt.transparent)
        p = QPainter(pix)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)
        p.setBrush(QColor("#1f6feb"))
        p.drawEllipse(2, 2, 28, 28)
        p.setPen(QColor("white"))
        p.setFont(QFont("Segoe UI", 16, QFont.Bold))
        p.drawText(pix.rect(), Qt.AlignCenter, "E")
        p.end()
        return QIcon(pix)

    def _build_spinner_frames(self) -> list[QIcon]:
        """Genera N frame con un arco rotante (effetto spinner)."""
        frames, steps = [], 8
        for i in range(steps):
            pix = QPixmap(32, 32)
            pix.fill(Qt.transparent)
            p = QPainter(pix)
            p.setRenderHint(QPainter.Antialiasing)
            p.setPen(Qt.NoPen)
            p.setBrush(QColor("#1f6feb"))
            p.drawEllipse(2, 2, 28, 28)
            p.setPen(QPen(QColor("white"), 3))
            p.setBrush(Qt.NoBrush)
            p.drawArc(7, 7, 18, 18, i * (360 // steps) * 16, 100 * 16)
            p.end()
            frames.append(QIcon(pix))
        return frames

    def _next_frame(self) -> None:
        self._frame_idx = (self._frame_idx + 1) % len(self._frames)
        self.setIcon(self._frames[self._frame_idx])

    def _maybe_start_spinner(self) -> None:
        if not self._spin_timer.isActive():
            self._spin_timer.start()

    def _stop_spinner_if_idle(self) -> None:
        if not self._running_names and self._spin_timer.isActive():
            self._spin_timer.stop()
            self.setIcon(self._static_icon)

    # ------------------------------------------------------------------
    def _build_base_menu(self) -> None:
        self.menu = QMenu()
        self._separator = self.menu.addSeparator()

        self.reload_action = QAction("🔄 Ricarica Workflows")
        self.reload_action.triggered.connect(lambda: self.reload_workflows(soft=False))
        self.menu.addAction(self.reload_action)

        self.apex_action = QAction("🧠 Genera Prompt (APEX-7)")
        self.apex_action.triggered.connect(self.generate_prompt)
        self.menu.addAction(self.apex_action)

        self.log_action = QAction("📜 Apri Log")
        self.log_action.triggered.connect(self.open_log)
        self.menu.addAction(self.log_action)

        self.info_action = QAction("ℹ️ Info")
        self.info_action.triggered.connect(self.show_info)
        self.menu.addAction(self.info_action)

        self.exit_action = QAction("⏻ Esci")
        self.exit_action.triggered.connect(self.quit_app)
        self.menu.addAction(self.exit_action)

        self.setContextMenu(self.menu)

    # ------------------------------------------------------------------
    #  CONFIG / DYNAMIC MENU
    # ------------------------------------------------------------------
    def load_workflows(self) -> None:
        path = Path(__file__).resolve().parent / self.CONFIG_FILE
        self._config_path = str(path)

        if not path.is_file():
            self.showMessage("Empire Desk", f"{self.CONFIG_FILE} non trovato.",
                             QSystemTrayIcon.Warning, 4000)
            self.workflows = []
            return

        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception as exc:
            self.workflows = []
            self.showMessage("Empire Desk", f"Errore parsing {self.CONFIG_FILE}: {exc}",
                             QSystemTrayIcon.Critical, 5000)
            return

        if isinstance(data, list):
            self.workflows, settings = data, {}
        else:
            self.workflows = data.get("workflows", [])
            settings = data.get("settings", {})

        if not isinstance(self.workflows, list):
            self.workflows = []
            self.showMessage("Empire Desk", "Campo 'workflows' non valido.",
                             QSystemTrayIcon.Critical, 5000)
            return

        self.runner.configure(settings.get("python", "auto"))
        self._auto_reload = bool(settings.get("auto_reload", True))
        self._max_concurrent = int(settings.get("max_concurrent", 4)) or 1
        self._setup_logging(settings.get("log_file", ""))

        # (Ri)aggancia il watcher alla config.
        if self._config_path not in self._watcher.files():
            self._watcher.addPath(self._config_path)

    def _setup_logging(self, log_file: str) -> None:
        if not log_file:
            self._log_file = None
            return
        self._log_file = str(Path(__file__).resolve().parent / log_file)
        LOGGER.setLevel(logging.INFO)
        if not any(isinstance(h, logging.FileHandler) for h in LOGGER.handlers):
            try:
                h = logging.FileHandler(self._log_file, encoding="utf-8")
                h.setFormatter(logging.Formatter(
                    "%(asctime)s | %(levelname)-7s | %(message)s"))
                LOGGER.addHandler(h)
            except Exception as exc:
                self._log_file = None
                self.showMessage("Empire Desk", f"Log non scrivibile: {exc}",
                                 QSystemTrayIcon.Warning, 4000)

    def populate_workflows(self) -> None:
        for act in self._dynamic_actions:
            self.menu.removeAction(act)
        self._dynamic_actions.clear()
        self._name_to_action.clear()

        for wf in self.workflows:
            name = wf.get("name", "<senza nome>")
            enabled = wf.get("enabled", True)
            action = QAction(name if enabled else f"🚫 {name}")
            action.setEnabled(bool(enabled))
            action.triggered.connect(
                lambda _c=False, w=wf: self._handle_click(w))
            self.menu.insertAction(self._separator, action)
            self._dynamic_actions.append(action)
            self._name_to_action[name] = action

    # ------------------------------------------------------------------
    #  RUN / STOP / QUEUE
    # ------------------------------------------------------------------
    def _handle_click(self, workflow: dict) -> None:
        name = workflow.get("name", "")
        if name in self._running_names:
            self.runner.stop(name)
        else:
            self._request_run(workflow)

    def _request_run(self, workflow: dict) -> None:
        if len(self._running_names) >= self._max_concurrent:
            self._queue.append(workflow)
            self.showMessage("Empire Desk",
                             f"Accodato (slot pieni): {workflow.get('name')}",
                             QSystemTrayIcon.Information, 2500)
        else:
            self._start(workflow)

    def _start(self, workflow: dict) -> None:
        name = workflow.get("name", "")
        self._running_names.add(name)
        self._refresh_action(name, running=True)
        self._update_tooltip()
        self._maybe_start_spinner()
        self.runner.run(workflow)

    def _pump_queue(self) -> None:
        while self._queue and len(self._running_names) < self._max_concurrent:
            self._start(self._queue.pop(0))

    @Slot(str, bool, str)
    def _on_workflow_finished(self, name: str, success: bool, detail: str) -> None:
        self._running_names.discard(name)
        self._refresh_action(name, running=False)
        self._update_tooltip()
        self._stop_spinner_if_idle()

        if self._log_file:
            LOGGER.info("WORKFLOW %s | success=%s | %s",
                        name, success, detail.replace("\n", " "))

        if success:
            self.showMessage("✅ Workflow Completato", f"{name}\n{detail}",
                             QSystemTrayIcon.Information, 5000)
        else:
            self.showMessage("❌ Errore nel Workflow", f"{name}\n{detail}",
                             QSystemTrayIcon.Critical, 6000)

        self._pump_queue()

    def _refresh_action(self, name: str, running: bool) -> None:
        action = self._name_to_action.get(name)
        if action is None:
            return
        if running:
            action.setText(f"⏹ {name}")
        else:
            wf = next((w for w in self.workflows if w.get("name") == name), {})
            enabled = wf.get("enabled", True)
            action.setText(name if enabled else f"🚫 {name}")

    def _update_tooltip(self) -> None:
        n = len(self._running_names)
        q = len(self._queue)
        txt = "Empire Desk — Command Center"
        if n:
            txt += f"  •  {n} attivo/i"
        if q:
            txt += f"  •  {q} in coda"
        self.setToolTip(txt)

    # ------------------------------------------------------------------
    #  AUTO-RELOAD
    # ------------------------------------------------------------------
    def _on_config_changed(self, path: str) -> None:
        # Alcuni editor riscrivono il file: re-aggancia il watch se perso.
        if Path(path).is_file() and path not in self._watcher.files():
            self._watcher.addPath(path)
        if self._auto_reload:
            self.reload_workflows(soft=True)

    def reload_workflows(self, soft: bool = False) -> None:
        if not soft:
            self.runner.terminate_all()
            self._running_names.clear()
            self._queue.clear()

        self.load_workflows()
        self.populate_workflows()

        # Rippristina lo stato "running" sulle voci ancora attive.
        for name in list(self._running_names):
            self._refresh_action(name, running=True)
        self._update_tooltip()

        if not soft:
            self.showMessage("Empire Desk",
                             f"Ricaricati {len(self.workflows)} workflow.",
                             QSystemTrayIcon.Information, 3000)
        else:
            self.showMessage("Empire Desk", "Config ricaricata.",
                             QSystemTrayIcon.Information, 2000)

    # ------------------------------------------------------------------
    def open_log(self) -> None:
        if not self._log_file or not Path(self._log_file).is_file():
            self.showMessage("Empire Desk", "Nessun log disponibile.",
                             QSystemTrayIcon.Warning, 3000)
            return
        QDesktopServices.openUrl(QUrl.fromLocalFile(self._log_file))

    # ------------------------------------------------------------------
    #  APEX-7 INTEGRATION
    # ------------------------------------------------------------------
    def generate_prompt(self) -> None:
        """Chiede l'obiettivo e pilota l'Orchestrator APEX-7 in background."""
        goal, ok = QInputDialog.getText(
            None, "APEX-7", "Descrivi l'obiettivo / prompt da generare:")
        if not ok or not goal.strip():
            return

        self.showMessage("APEX-7", "Generazione in corso...",
                         QSystemTrayIcon.Information, 2000)
        db = str(Path(__file__).resolve().parent / "apex7_memory.db")
        self._apex_worker = ApexWorker(goal.strip(), db, self)
        self._apex_worker.result_ready.connect(self._on_apex_done)
        self._apex_worker.error_occurred.connect(self._on_apex_error)
        self._apex_worker.start()

    def _on_apex_done(self, draft: str, analysis: str) -> None:
        dlg = QDialog()
        dlg.setWindowTitle("APEX-7 — Output")
        layout = QVBoxLayout(dlg)
        te = QTextEdit()
        te.setReadOnly(True)
        te.setPlainText(f"{draft}\n\n--- ANALYSIS ---\n{analysis}")
        layout.addWidget(te)
        btn = QPushButton("Chiudi")
        btn.clicked.connect(dlg.accept)
        layout.addWidget(btn)
        dlg.resize(600, 420)
        dlg.exec()
        self.showMessage("APEX-7", "Prompt generato e salvato in memoria.",
                         QSystemTrayIcon.Information, 3000)

    def _on_apex_error(self, message: str) -> None:
        self.showMessage("APEX-7 — Errore", message,
                         QSystemTrayIcon.Critical, 6000)

    def show_info(self) -> None:
        QMessageBox.information(
            None, "Empire Desk",
            "Empire Desk — System Tray Command Center\n\n"
            "• Clic destro sull'icona = menu.\n"
            "• Clic su un workflow = avvialo.\n"
            "• Clic su un workflow ATTIVO = fermalo.\n"
            "• 'Ricarica Workflows' = reload da workflows.json.\n"
            f"• Max concorrenti: {self._max_concurrent}  •  Auto-reload: {self._auto_reload}"
        )

    def quit_app(self) -> None:
        QApplication.instance().quit()


# ===========================================================================
#  ENTRY POINT
# ===========================================================================
def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName("Empire Desk")
    app.setQuitOnLastWindowClosed(False)

    if hasattr(Qt, "AA_UseHighDpiPixmaps"):
        app.setAttribute(Qt.AA_UseHighDpiPixmaps)

    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "Empire Desk",
                             "System Tray non disponibile su questo sistema.")
        return 1

    desk = EmpireDesk()
    desk.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
