/**
 * Syncs theme preference between the mind map and MkDocs Material.
 * Mind map stores: localStorage 'ml-prep-theme' = 'dark' | 'light'
 * MkDocs stores: localStorage '__palette' = JSON with index (0=light, 1=dark)
 *
 * On docs page load: if mind map preference exists and differs, apply it.
 * On docs palette change: save to shared key so mind map picks it up.
 */
(function () {
  "use strict";

  function syncFromMindMap() {
    try {
      var mapTheme = localStorage.getItem("ml-prep-theme");
      if (!mapTheme) return;

      var palette = document.querySelector("[data-md-color-scheme]");
      if (!palette) return;

      var currentScheme = palette.getAttribute("data-md-color-scheme");
      var wantsDark = mapTheme === "dark";
      var isDark = currentScheme === "slate";

      if (wantsDark !== isDark) {
        // Click the palette toggle to switch
        var toggle = document.querySelector(
          'label[for="__palette_0"], label[for="__palette_1"]'
        );
        // Find the correct toggle — the one that would switch to our desired mode
        var inputs = document.querySelectorAll('input[name="__palette"]');
        for (var i = 0; i < inputs.length; i++) {
          var label = document.querySelector('label[for="' + inputs[i].id + '"]');
          if (label) {
            var title = label.getAttribute("title") || "";
            if (wantsDark && title.indexOf("dark") !== -1) {
              inputs[i].click();
              break;
            } else if (!wantsDark && title.indexOf("light") !== -1) {
              inputs[i].click();
              break;
            }
          }
        }
      }
    } catch (e) {}
  }

  // Watch for MkDocs palette changes and save to shared key
  function watchPaletteChanges() {
    var observer = new MutationObserver(function () {
      try {
        var scheme = document.body.getAttribute("data-md-color-scheme");
        if (scheme) {
          localStorage.setItem(
            "ml-prep-theme",
            scheme === "slate" ? "dark" : "light"
          );
        }
      } catch (e) {}
    });

    observer.observe(document.body, {
      attributes: true,
      attributeFilter: ["data-md-color-scheme"],
    });
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(function () {
      setTimeout(syncFromMindMap, 100);
      watchPaletteChanges();
    });
  } else {
    document.addEventListener("DOMContentLoaded", function () {
      setTimeout(syncFromMindMap, 100);
      watchPaletteChanges();
    });
  }
})();
