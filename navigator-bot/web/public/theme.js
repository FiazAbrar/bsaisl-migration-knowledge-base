/* Sets the saved colour theme before the page is drawn, so it never flashes the wrong colours.
   Loaded without defer, and kept tiny. "light" or "dark" is a choice the visitor made; nothing saved
   means "follow the phone's setting". */
(function () {
  try {
    var t = localStorage.getItem("navigator.theme");
    if (t === "light" || t === "dark") document.documentElement.setAttribute("data-theme", t);
  } catch (e) { /* storage blocked: follow the phone's setting */ }
})();
