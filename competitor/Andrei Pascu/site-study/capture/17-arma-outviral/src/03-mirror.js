/* fonte: https://armageddon.bsns.it/assets/mirror.js */
/* Behaviour the mirrored pages need back.

   The pages are the originals from andrei-copy.com with every Squarespace
   script removed, so anything the platform drove in JavaScript stopped
   working. The accordions are the only piece of that which carries content —
   the lesson lists live inside them and the page tells you to click. This
   reproduces exactly what the Squarespace accordion component did: it flips
   aria-expanded, adds the --open class the stylesheet keys off, and sets
   data-is-open so the plus turns into a minus. */

(function () {
  "use strict";

  function setItem(button, open) {
    var item = button.closest(".accordion-item");
    var dropdown = document.getElementById(button.getAttribute("aria-controls"));
    button.setAttribute("aria-expanded", open ? "true" : "false");
    if (item) item.setAttribute("data-is-open", open ? "true" : "false");
    if (dropdown) dropdown.classList.toggle("accordion-item__dropdown--open", open);
  }

  document.querySelectorAll(".accordion-items-container").forEach(function (list) {
    var multiple = list.getAttribute("data-should-allow-multiple-open-items") === "true";
    var buttons = list.querySelectorAll(".accordion-item__click-target");

    buttons.forEach(function (button) {
      // Whatever state the page was saved in is the state it opens in.
      var dropdown = document.getElementById(button.getAttribute("aria-controls"));
      var open = dropdown
        ? dropdown.classList.contains("accordion-item__dropdown--open")
        : button.getAttribute("aria-expanded") === "true";
      setItem(button, open);

      button.addEventListener("click", function (e) {
        e.preventDefault();
        var nowOpen = button.getAttribute("aria-expanded") !== "true";
        if (nowOpen && !multiple) {
          buttons.forEach(function (other) {
            if (other !== button) setItem(other, false);
          });
        }
        setItem(button, nowOpen);
      });
    });
  });
})();

/* Image boxes.

   Squarespace's image component measures its own grid cell in JavaScript and
   writes the fitted size back as --image-component-container-width/height.
   The captured markup carries the numbers it computed at 1440px wide, so at
   any other width the images kept their desktop size and stretched the Fluid
   Engine rows. This recomputes them exactly as the component does:

     cover            -> the whole cell
     contain, wide    -> full width, height = width / aspect
     contain, tall    -> full height, width  = height * aspect

   Measuring happens with the boxes collapsed, so an image can never inflate
   the row it is being measured against. */

(function () {
  "use strict";

  var roots = [].slice.call(
    document.querySelectorAll(".fluid-image-component-root"));
  if (!roots.length) return;

  function aspectOf(root) {
    var raw = getComputedStyle(root)
      .getPropertyValue("--image-component-native-aspect-ratio").trim();
    if (!raw) return null;
    var parts = raw.split("/");
    var value = parts.length === 2
      ? parseFloat(parts[0]) / parseFloat(parts[1])
      : parseFloat(raw);
    return value > 0 && isFinite(value) ? value : null;
  }

  function fitAll() {
    roots.forEach(function (root) {
      root.style.setProperty("--image-component-container-width", "0px");
      root.style.setProperty("--image-component-container-height", "0px");
    });

    var cells = roots.map(function (root) {
      var box = root.closest(".fe-block") || root.parentElement;
      var rect = box.getBoundingClientRect();
      return { w: rect.width, h: rect.height };
    });

    roots.forEach(function (root, i) {
      var cell = cells[i];
      var fit = getComputedStyle(root)
        .getPropertyValue("--image-component-object-fit").trim();
      var aspect = aspectOf(root);
      var width = "100%";
      var height = "100%";
      if (fit !== "cover" && aspect && cell.w > 0 && cell.h > 0) {
        if (cell.w / aspect <= cell.h) height = (cell.w / aspect) + "px";
        else width = (cell.h * aspect) + "px";
      }
      root.style.setProperty("--image-component-container-width", width);
      root.style.setProperty("--image-component-container-height", height);
    });
  }

  var pending = null;
  function schedule() {
    clearTimeout(pending);
    pending = setTimeout(fitAll, 120);
  }

  fitAll();
  window.addEventListener("resize", schedule);
  window.addEventListener("load", fitAll);
})();

/* Scaled headlines.

   Squarespace's "scaled text" makes a headline fill the width of its block by
   measuring the line and writing a font-size onto the wrapping span. The
   captured pages carry the sizes it computed at 1440px wide, so on a phone the
   headlines stayed desktop-sized and overflowed. This measures and rewrites
   them the same way, on load and on resize. */

(function () {
  "use strict";

  var spans = [].slice.call(
    document.querySelectorAll(".sqsrte-scaled-text-container > .sqsrte-scaled-text"));
  if (!spans.length) return;

  var REFERENCE = 100;

  function scale(span) {
    var box = span.parentElement;
    var target = box.clientWidth;
    if (!target) return;

    var line = span.firstElementChild || span;
    var style = line.getAttribute("style") || "";
    span.style.fontSize = REFERENCE + "px";
    line.style.whiteSpace = "pre";
    line.style.width = "max-content";
    var natural = line.getBoundingClientRect().width;
    line.setAttribute("style", style);

    if (natural > 0) {
      span.style.fontSize = Math.round(REFERENCE * target / natural * 10) / 10 + "px";
    }
  }

  function scaleAll() {
    spans.forEach(scale);
  }

  var pending = null;
  scaleAll();
  window.addEventListener("load", scaleAll);
  document.fonts.ready.then(scaleAll);
  window.addEventListener("resize", function () {
    clearTimeout(pending);
    pending = setTimeout(scaleAll, 120);
  });
})();

/* Armageddon price treatment.

   These four products are no longer sold on their own — they only come inside
   the €199 Armageddon pack — so every standalone price on the page has to be
   struck through and labelled.

   Three of the four print their price inside the card artwork rather than as
   text, so the rule is drawn over the artwork. The coordinates below are the
   price glyphs' bounding box measured in the source file's own pixels; they
   are mapped onto whatever box the image ends up in, honouring object-fit, so
   the rule stays on the price at any width. outViral prints a real price, so
   that one is struck with text-decoration instead.

   The label goes into the pricing block underneath, which is normal flow —
   the cards themselves sit in Fluid Engine grid cells that must not grow. */

(function () {
  "use strict";

  var LABEL = "Incluso nel pacchetto Armageddon";

  /* price glyphs, in the source image's own pixels */
  var CARDS = [
    { file: "Artboard--E2-80-93-100", nat: [1501, 2052], box: [492, 1600, 912, 1750] },
    { file: "Artboard--E2-80-93-99-min", nat: [1600, 1375], box: [297, 827, 669, 1009] },
    { file: "Artboard--E2-80-93-96", nat: [930, 799], box: [173, 481, 389, 586] }
  ];

  function sourceOf(el) {
    if (el.tagName === "IMG") return el.currentSrc || el.getAttribute("src") || "";
    return getComputedStyle(el).backgroundImage || "";
  }

  function fitOf(el) {
    if (el.tagName === "IMG") return getComputedStyle(el).objectFit || "fill";
    var size = getComputedStyle(el).backgroundSize || "auto";
    return size.indexOf("cover") > -1 ? "cover"
      : size.indexOf("contain") > -1 ? "contain" : "fill";
  }

  /* Where the source image actually lands inside its box. */
  function painted(box, nat, fit) {
    var scale;
    if (fit === "cover") scale = Math.max(box.w / nat[0], box.h / nat[1]);
    else if (fit === "contain") scale = Math.min(box.w / nat[0], box.h / nat[1]);
    else return { x: 0, y: 0, sx: box.w / nat[0], sy: box.h / nat[1] };
    return {
      x: (box.w - nat[0] * scale) / 2,
      y: (box.h - nat[1] * scale) / 2,
      sx: scale, sy: scale
    };
  }

  var placed = [];

  CARDS.forEach(function (card) {
    var el = null;
    var all = document.querySelectorAll("img, .card");
    for (var i = 0; i < all.length; i++) {
      if (sourceOf(all[i]).indexOf(card.file) > -1) { el = all[i]; break; }
    }
    if (!el) return;

    /* The rule goes on <body>, in page coordinates. Giving the image's own
       container a position would make it the containing block for the
       absolutely positioned artwork, and the fluid image component sizes that
       artwork with height:100% — on outHeadline that collapsed the card to
       nothing. Nothing of the original is touched this way. */
    var rule = document.createElement("span");
    rule.className = "ag-strike";
    rule.setAttribute("aria-hidden", "true");
    document.body.appendChild(rule);
    placed.push({ el: el, rule: rule, card: card });
  });

  function position() {
    var ox = window.pageXOffset, oy = window.pageYOffset;
    placed.forEach(function (p) {
      var er = p.el.getBoundingClientRect();
      if (!er.width || !er.height) { p.rule.style.display = "none"; return; }
      p.rule.style.display = "";
      var fit = painted({ w: er.width, h: er.height }, p.card.nat, fitOf(p.el));
      var b = p.card.box;
      var left = er.left + ox + fit.x + b[0] * fit.sx;
      var right = er.left + ox + fit.x + b[2] * fit.sx;
      var mid = er.top + oy + fit.y + ((b[1] + b[3]) / 2) * fit.sy;
      var thick = Math.max(2, (b[3] - b[1]) * fit.sy * 0.16);
      var pad = (right - left) * 0.06;      /* overshoot, the way a pen would */
      p.rule.style.left = (left - pad) + "px";
      p.rule.style.width = (right - left + pad * 2) + "px";
      p.rule.style.top = (mid - thick / 2) + "px";
      p.rule.style.height = thick + "px";
    });
  }

  /* outViral prints a real price. */
  document.querySelectorAll(".pricing-plan-price-amount").forEach(function (el) {
    el.classList.add("ag-struck-text");
  });

  /* Is this panel dark? The mirrored pages already answer that in their own
     ink: a section relit dark carries light text. Read the colour the block
     inherits rather than guessing at the backdrop. */
  function onDark(el) {
    var m = /(\d+),\s*(\d+),\s*(\d+)/.exec(getComputedStyle(el).color);
    if (!m) return false;
    var c = [m[1], m[2], m[3]].map(function (v) {
      v = v / 255;
      return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2] > 0.35;
  }

  /* The label lives in the pricing block, which is ordinary flow. */
  document.querySelectorAll(".sqs-block-pricing-plan .productDetails")
    .forEach(function (details) {
      if (details.querySelector(".ag-incluso")) return;
      if (onDark(details)) details.classList.add("ag-on-dark");
      var note = document.createElement("p");
      note.className = "ag-incluso";
      note.textContent = LABEL;
      var button = details.querySelector("button, .sqs-button-element--primary");
      if (button) details.insertBefore(note, button);
      else details.appendChild(note);
    });

  if (placed.length) {
    var pending = null;
    position();
    window.addEventListener("load", position);
    document.fonts.ready.then(position);
    window.addEventListener("resize", function () {
      clearTimeout(pending);
      pending = setTimeout(position, 120);
    });
    /* The artwork may still be decoding when this runs. */
    placed.forEach(function (p) {
      if (p.el.tagName === "IMG" && !p.el.complete) {
        p.el.addEventListener("load", position);
      }
    });
  }
})();

/* Back should leave the page, not undo a scroll.

   These pages navigate themselves with in-page anchors — outFunnel alone has
   four ("Sono un copywriter", "Sono un media buyer" …) and every product page
   has two or three that jump to the price. Each click pushes a history entry,
   so someone who reads through a page and then hits Back gets their own scroll
   positions replayed at them one press at a time before the browser will go
   anywhere. Andrei reported it as having to press Back several times.

   So: scroll to the target, then *replace* the history entry instead of adding
   one. The hash still ends up in the address bar, deep links still work, and
   Back means the previous page. Modifier-clicks and new-tab clicks are left
   alone. */

(function () {
  "use strict";

  document.addEventListener("click", function (e) {
    if (e.defaultPrevented || e.button !== 0) return;
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;

    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a || a.target === "_blank") return;

    var hash = a.getAttribute("href");
    if (hash === "#") {                 // a link the mirror neutralised
      e.preventDefault();               // and which would otherwise stack up
      return;
    }

    var target = document.getElementById(hash.slice(1)) ||
      document.querySelector('[name="' + hash.slice(1) + '"]');
    if (!target) return;

    e.preventDefault();
    target.scrollIntoView({ behavior: "smooth", block: "start" });
    if (history.replaceState) history.replaceState(null, "", hash);
    else window.location.hash = hash;
  });
})();
