/**
 * Custom expandable TOC for the KB fundamentals page.
 *
 * MkDocs Material's default TOC only shows H2/H3 under the first H1.
 * This script replaces it with an accordion TOC:
 * - All H1 topics listed (collapsed by default)
 * - Active topic expands to show its H2 subtopics
 * - Scroll spy auto-expands the current section
 */
(function () {
  "use strict";

  var KB_PATH = "knowledge-base/ml-ds-llm-fundamentals";

  function isKBPage() {
    return window.location.pathname.indexOf(KB_PATH) !== -1;
  }

  /**
   * Collect H2s that belong to a given H1 (everything between this H1 and the next H1).
   */
  function getH2sForH1(h1, allH1Set) {
    var h2s = [];
    var sibling = h1.nextElementSibling;
    while (sibling) {
      if (sibling.tagName === "H1" && allH1Set.has(sibling)) break;
      if (sibling.tagName === "H2" && sibling.id) {
        h2s.push({
          id: sibling.id,
          text: sibling.textContent.replace(/[¶🧠]/g, "").trim(),
          top: sibling.offsetTop,
        });
      }
      sibling = sibling.nextElementSibling;
    }
    return h2s;
  }

  function buildCustomTOC() {
    if (!isKBPage()) return;

    var tocContainer = document.querySelector(".md-sidebar--secondary");
    if (!tocContainer) return;

    var h1s = document.querySelectorAll("article h1[id]");
    if (h1s.length < 2) return;

    var h1Set = new Set(h1s);

    // Build topic data with H2 children
    var topics = [];
    for (var i = 0; i < h1s.length; i++) {
      var h1 = h1s[i];
      topics.push({
        id: h1.getAttribute("id"),
        text: h1.textContent.replace(/[¶🧠]/g, "").trim(),
        top: h1.offsetTop,
        h2s: getH2sForH1(h1, h1Set),
      });
    }

    // Build HTML
    var html =
      '<nav class="md-nav md-nav--secondary custom-kb-toc" aria-label="Topics">' +
      '<label class="md-nav__title">Topics (' + topics.length + ")</label>" +
      '<ul class="md-nav__list custom-toc-list" data-md-component="toc">';

    for (var t = 0; t < topics.length; t++) {
      var topic = topics[t];
      html +=
        '<li class="md-nav__item toc-topic" data-topic-id="' + topic.id + '">' +
        '<a href="#' + topic.id + '" class="md-nav__link custom-toc-link toc-h1" data-toc-id="' + topic.id + '">' +
        '<span class="md-ellipsis">' + topic.text + "</span>";

      if (topic.h2s.length > 0) {
        html += '<span class="toc-count">' + topic.h2s.length + "</span>";
      }
      html += "</a>";

      // H2 children (hidden by default)
      if (topic.h2s.length > 0) {
        html += '<ul class="toc-h2-list">';
        for (var h = 0; h < topic.h2s.length; h++) {
          html +=
            '<li class="md-nav__item">' +
            '<a href="#' + topic.h2s[h].id + '" class="md-nav__link custom-toc-link toc-h2" data-toc-id="' + topic.h2s[h].id + '">' +
            '<span class="md-ellipsis">' + topic.h2s[h].text + "</span>" +
            "</a></li>";
        }
        html += "</ul>";
      }

      html += "</li>";
    }

    html += "</ul></nav>";

    // Replace the default TOC
    var inner = tocContainer.querySelector(".md-sidebar__inner");
    if (inner) {
      inner.innerHTML = html;
    }

    // Inject styles and reveal
    injectStyles();
    showTOC();

    // Setup scroll spy
    setupScrollSpy(topics);
  }

  // Show the TOC sidebar (CSS hides it by default to prevent flash)
  function showTOC() {
    var inner = document.querySelector(".md-sidebar--secondary .md-sidebar__inner");
    if (inner) inner.style.visibility = "visible";
  }

  function injectStyles() {
    if (document.getElementById("kb-toc-styles")) return;

    var style = document.createElement("style");
    style.id = "kb-toc-styles";
    style.textContent =
      /* Container */
      ".custom-kb-toc { padding-top: 0; }" +
      ".custom-kb-toc .md-nav__title { font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; padding: 0.6rem 0.6rem 0.4rem; color: var(--md-default-fg-color--light); }" +
      ".custom-toc-list { max-height: calc(100vh - 6rem); overflow-y: auto; scrollbar-width: thin; padding: 0 0.2rem; }" +
      ".custom-toc-list::-webkit-scrollbar { width: 3px; }" +
      ".custom-toc-list::-webkit-scrollbar-thumb { background: var(--md-default-fg-color--lightest); border-radius: 3px; }" +
      "@media (min-width: 76.25em) { .md-sidebar--secondary { width: 14rem; } }" +

      /* H1 topic links */
      ".toc-h1 { font-size: 0.7rem !important; padding: 0.25rem 0.5rem !important; line-height: 1.4 !important; min-height: 36px; border-left: 2px solid transparent; transition: all 0.15s; display: flex; align-items: center; justify-content: space-between; gap: 4px; }" +
      ".toc-h1:hover { border-left-color: var(--md-accent-fg-color); background: var(--md-code-bg-color); }" +
      ".toc-h1.active { border-left-color: var(--md-accent-fg-color); color: var(--md-accent-fg-color) !important; font-weight: 600; background: var(--md-code-bg-color); }" +

      /* H2 count badge */
      ".toc-count { font-size: 0.5rem; background: var(--md-default-fg-color--lightest); color: var(--md-default-fg-color--light); border-radius: 3px; padding: 0 4px; min-width: 16px; text-align: center; flex-shrink: 0; }" +
      ".toc-topic.expanded .toc-count { background: var(--md-accent-fg-color); color: white; }" +

      /* H2 subtopic list — hidden by default, expand on active */
      ".toc-h2-list { display: none; padding-left: 0.5rem; margin: 0; list-style: none; overflow: hidden; transition: max-height 0.25s ease; }" +
      ".toc-topic.expanded .toc-h2-list { display: block; }" +

      /* H2 subtopic links */
      ".toc-h2 { font-size: 0.65rem !important; padding: 0.15rem 0.5rem 0.15rem 0.7rem !important; line-height: 1.3 !important; min-height: 32px; display: flex; align-items: center; color: var(--md-default-fg-color--light) !important; border-left: 1px solid var(--md-default-fg-color--lightest); transition: all 0.15s; }" +
      ".toc-h2:hover { color: var(--md-default-fg-color) !important; border-left-color: var(--md-accent-fg-color); }" +
      ".toc-h2.active { color: var(--md-accent-fg-color) !important; border-left-color: var(--md-accent-fg-color); font-weight: 500; }";

    document.head.appendChild(style);
  }

  function setupScrollSpy(topics) {
    var ticking = false;
    var lastActiveTopicId = null;

    // Build a flat list of heading references (positions read live at scroll time)
    var allHeadings = [];
    for (var t = 0; t < topics.length; t++) {
      allHeadings.push({ id: topics[t].id, type: "h1", topicId: topics[t].id });
      for (var h = 0; h < topics[t].h2s.length; h++) {
        allHeadings.push({ id: topics[t].h2s[h].id, type: "h2", topicId: topics[t].id });
      }
    }

    function onScroll() {
      if (ticking) return;
      ticking = true;

      requestAnimationFrame(function () {
        var scrollTop = window.scrollY + 140;
        var currentHeading = allHeadings[0];

        // Read positions live from DOM (MathJax/images may have shifted content)
        for (var i = allHeadings.length - 1; i >= 0; i--) {
          var el = document.getElementById(allHeadings[i].id);
          if (el && scrollTop >= el.offsetTop) {
            currentHeading = allHeadings[i];
            break;
          }
        }

        if (!currentHeading) { ticking = false; return; }

        var activeTopicId = currentHeading.topicId;
        var activeHeadingId = currentHeading.id;

        // Only update DOM if the active topic changed
        if (activeTopicId !== lastActiveTopicId) {
          lastActiveTopicId = activeTopicId;

          // Expand/collapse topics
          var topicEls = document.querySelectorAll(".toc-topic");
          for (var j = 0; j < topicEls.length; j++) {
            var isExpanded = topicEls[j].getAttribute("data-topic-id") === activeTopicId;
            topicEls[j].classList.toggle("expanded", isExpanded);
          }
        }

        // Update active link highlighting (H1 and H2)
        var allLinks = document.querySelectorAll(".custom-toc-link");
        for (var k = 0; k < allLinks.length; k++) {
          var linkId = allLinks[k].getAttribute("data-toc-id");
          var isH1Active = linkId === activeTopicId && allLinks[k].classList.contains("toc-h1");
          var isH2Active = linkId === activeHeadingId && allLinks[k].classList.contains("toc-h2");
          allLinks[k].classList.toggle("active", isH1Active || isH2Active);
        }

        // Auto-scroll TOC to keep active H1 visible
        var activeH1Link = document.querySelector('.toc-h1[data-toc-id="' + activeTopicId + '"]');
        if (activeH1Link) {
          var list = activeH1Link.closest(".custom-toc-list");
          if (list) {
            var linkTop = activeH1Link.offsetTop - list.offsetTop;
            var listScroll = list.scrollTop;
            var listHeight = list.clientHeight;
            if (linkTop < listScroll + 30 || linkTop > listScroll + listHeight - 60) {
              list.scrollTo({ top: linkTop - listHeight / 4, behavior: "smooth" });
            }
          }
        }

        ticking = false;
      });
    }

    window.addEventListener("scroll", onScroll, { passive: true });

    // Also allow click to expand (in addition to scroll spy)
    document.querySelectorAll(".toc-h1").forEach(function (link) {
      link.addEventListener("click", function () {
        var topicId = this.getAttribute("data-toc-id");
        var topicEls = document.querySelectorAll(".toc-topic");
        for (var j = 0; j < topicEls.length; j++) {
          var shouldExpand = topicEls[j].getAttribute("data-topic-id") === topicId;
          topicEls[j].classList.toggle("expanded", shouldExpand);
        }
        lastActiveTopicId = topicId;
      });
    });

    // Initial highlight
    setTimeout(onScroll, 200);
  }

  // MkDocs Material instant navigation support
  // CSS hides TOC by default (prevents flash). JS shows it:
  // - KB page: after building custom TOC (via buildCustomTOC → showTOC)
  // - Other pages: immediately
  function initTOC() {
    if (isKBPage()) {
      buildCustomTOC();
    } else {
      showTOC();
    }
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(initTOC);
  } else {
    document.addEventListener("DOMContentLoaded", initTOC);
  }
})();
