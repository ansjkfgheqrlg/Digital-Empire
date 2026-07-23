from empire.tools.builtins.filesystem import register_filesystem_tools
from empire.tools.builtins.shell import register_shell_tools
from empire.tools.builtins.system import register_system_tools

def register_all_builtin_tools(registry):
    register_filesystem_tools(registry)
    register_shell_tools(registry)
    register_system_tools(registry)

__all__ = ["register_all_builtin_tools"]
