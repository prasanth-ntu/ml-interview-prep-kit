# Overview Page Prototypes

Three interactive overview page prototypes for the ML Interview Prep Kit. Each visualizes all resources (Knowledge Base, System Design, Coding Practice, Career Frameworks, Interview Tracking, AI Workflows) in a distinct style.

## Prototypes

| File | Style | Description |
|------|-------|-------------|
| `bento.html` | **Bento Grid** | Apple-style editorial layout with glassmorphism tiles, animated counters, scroll reveals, command palette (Cmd+K) |
| `skilltree.html` | **Skill Tree / RPG** | Radial tech tree with glowing nodes, animated energy flow, starfield background, branch filtering |
| `mission.html` | **Mission Control** | NASA/SpaceX command center with boot sequence, scan lines, pulsing LEDs, system panels (dark-only) |

## How to Preview

Open any HTML file directly in a browser:

```bash
open overview-prototypes/bento.html
open overview-prototypes/skilltree.html
open overview-prototypes/mission.html
```

All prototypes load KB data from `../ml-knowledge-map-data.js` (the shared source of truth). Run `make kb-sync` if topics have been updated.

## Next Steps

1. Pick a winner (or combine elements from multiple prototypes)
2. Rename/copy winner to `overview.html` at repo root
3. Integrate with build system:
   - Add "Overview" nav link to `index.html` top bar
   - Update `Makefile` serve target to include `/overview/`
   - Update `.github/workflows/pages.yml` to deploy to `/overview/`
4. Final URL: `interview.prasanth.io/overview/`
