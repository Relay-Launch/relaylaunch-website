# Blueprints — AI-Assisted Development Resources

This folder contains architecture documents, specifications, and reference
materials that AI coding tools (Claude Code, GitHub Copilot, etc.) should
consult when generating or reviewing code in this repository.

## How It Works

When starting a build session, point your AI tool at this folder:

- **Claude Code:** `@docs/blueprints` or reference files directly
- **GitHub Copilot:** Files here are indexed automatically via workspace context
- **Any AI tool:** Upload or reference these documents at the start of a session

## Folder Structure

Place documents in the appropriate subfolder:

```
docs/blueprints/
├── README.md              ← You are here
├── architecture/          ← System design, tech stack decisions, data flow diagrams
├── api-contracts/         ← Shared API schemas, webhook payloads, endpoint specs
├── requirements/          ← Feature specs, user stories, acceptance criteria
└── shared-standards/      ← Brand guidelines, coding conventions, design tokens
```

Create subfolders as needed. Use Markdown (`.md`) for maximum AI tool compatibility.

## What to Put Here

- **Architecture docs** — system diagrams, infrastructure decisions, deployment topology
- **API contracts** — request/response schemas shared between website and Command Center
- **Feature requirements** — detailed specs before starting implementation
- **Design tokens** — shared color, typography, and spacing references
- **Integration specs** — how this repo connects to `relaylaunch-control-center`

## Cross-Repo Context

This repository (`relaylaunch-website`) is the public-facing marketing site.
It works alongside the **Command Center** (`relaylaunch-control-center`),
which is the internal client/operations dashboard.

For shared context between repos, maintain parallel `docs/blueprints/` folders
in both repositories. Documents that define the interface between the two
systems (API contracts, shared data models, webhook specs) should exist in
both repos so each AI tool has full context regardless of which repo it is
working in.

**Keeping specs in sync:** Pick one repo as the source of truth for each
shared document (typically the repo that owns the API endpoint). Copy the
spec to the other repo and note at the top which repo holds the canonical
version. When the spec changes, update the source first, then copy it over.

## Tips for Blueprint-Driven Development

1. **Upload first, build second** — Add your specs to this folder before
   asking the AI to implement them
2. **Be specific** — Include acceptance criteria, edge cases, and examples
3. **Keep docs current** — Update blueprints when requirements change
4. **Reference in prompts** — Tell the AI to "read docs/blueprints/[file]
   before implementing"
5. **Cross-link repos** — When a feature spans both repos, note the
   counterpart in each blueprint
