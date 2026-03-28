/**
 * Injects "View in Mind Map" links next to H1 headings in the KB fundamentals page.
 * Works with MkDocs Material — runs after page load.
 *
 * Only activates on the ml-ds-llm-fundamentals page.
 */
(function () {
  "use strict";

  const MAP_BASE_URL = "/";
  const KB_PATH = "knowledge-base/ml-ds-llm-fundamentals/";

  function isKBPage() {
    return window.location.pathname.includes(KB_PATH);
  }

  function slugToNodeName(slug) {
    // Convert MkDocs heading slug back to approximate node name
    // e.g., "transformer-architecture" → "Transformer Architecture"
    return slug
      .replace(/-+/g, " ")
      .replace(/\b\w/g, (c) => c.toUpperCase())
      .replace(/ And /g, " & ")
      .replace(/ Or /g, " / ");
  }

  function injectMapLinks() {
    if (!isKBPage()) return;

    // Target H1 headings (which are topic-level in the KB)
    const headings = document.querySelectorAll(
      ".md-content h1[id], .md-content h2[id]"
    );

    headings.forEach(function (heading) {
      const id = heading.getAttribute("id");
      if (!id) return;

      // Skip non-topic headings (like "Quick Navigation", "Detailed Explanation")
      if (
        id === "ml-interview-prep-kit" ||
        id.startsWith("quick-") ||
        id.startsWith("detailed-")
      )
        return;

      const nodeName = slugToNodeName(id);
      const mapUrl = MAP_BASE_URL + "?focus=" + encodeURIComponent(nodeName);

      const link = document.createElement("a");
      link.href = mapUrl;
      link.title = "View in Mind Map";
      link.className = "map-link";
      link.target = "_blank";
      link.innerHTML = " 🧠";
      link.style.cssText =
        "text-decoration:none;font-size:0.7em;opacity:0.4;transition:opacity 0.2s;vertical-align:super;margin-left:4px;";

      link.addEventListener("mouseenter", function () {
        this.style.opacity = "1";
      });
      link.addEventListener("mouseleave", function () {
        this.style.opacity = "0.4";
      });

      heading.appendChild(link);
    });
  }

  // MkDocs Material uses instant navigation — re-inject on page change
  if (typeof document$ !== "undefined") {
    // MkDocs Material observable
    document$.subscribe(function () {
      injectMapLinks();
    });
  } else {
    // Fallback: run on DOMContentLoaded
    document.addEventListener("DOMContentLoaded", injectMapLinks);
  }
})();
