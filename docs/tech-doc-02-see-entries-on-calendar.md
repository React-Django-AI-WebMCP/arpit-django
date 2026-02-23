# Technical Document: See Entries on Calendar

**Subtask (from ClickUp):** See entries on calendar  
**User Story:** Story 2 – See time entries on the calendar  
**Sources:** `calendar-module-requirement-and-ui.md`, `calendar-module-epic.md`, `calendar-module-user-stories.md`  
**Design reference:** Figma 02.1 Time Tracker - Nexus, node 7369-75653 (entry blocks, labels, colours; empty state).

---

## Scope Boundary

**In scope**

- Time entries shown as **solid rectangular blocks** in the calendar grid (month view) or in day columns (week view).
- **Labels** on blocks (e.g. task or project name); content and truncation per requirement “best practice.”
- Entry **types or statuses** distinguished by **colour**.
- **Week view:** Entries can span one or more time slots or days; hourly markers on vertical axis (per Story 1).
- **Empty state:** When no entries in visible period: central message (e.g. “No entries yet”) and “Add Entry” button.

**Out of scope**

- Defining which entry types/statuses or how many colours (requirement does not list them).
- Defining exact label content, max length, truncation pattern, or tooltip (requirement defers to best practice).

---

## Frontend Blueprint

- **Entry blocks:** One rectangular block per time entry. Use **existing** card/block components if available; otherwise **NEEDS CLARIFICATION** before introducing a new component.
- **Label:** Task name or project name (per requirement). Truncation and tooltip: **best practice** (implementer’s choice); no invented rules.
- **Colour:** Map entry type/status to colour. **NEEDS CLARIFICATION:** Which types/statuses and colour set (see below).
- **Empty state:** Single central message + “Add Entry” button; use existing empty-state pattern if present.
- **Data:** Consume list of time entries for the visible period (date range). Fields only as in `calendar-module-data-schema.md`.

---

## Backend Blueprint

- **List time entries** for a date range (and optionally filters/scope as in Filter and scope doc). RESTful: e.g. `GET /api/calendar/entries/` with query params for start/end date (and later: project, task, user, scope).
- Response: project standard `success_response` with `data` containing list of entry objects. Field set exactly as in `calendar-module-data-schema.md`; no extra fields.
- Pagination: per project standards for list endpoints.

---

## Data Schema

- See **`calendar-module-data-schema.md`**. Entry payload must include at least: fields needed for placement (time/duration or start/end), label (task name or project), and type/status for colour. No additional invented fields.

---

## NEEDS CLARIFICATION

1. **Entry types/statuses and colours:** Requirement states “distinguished by colour” but does not list which entry types or statuses exist or how many colours. Needed for consistent UI and backend enum/choices.
2. **Label content and truncation:** Requirement defers to “best practice.” If a new component or new truncation rule is required, specify: max length, truncation pattern (e.g. ellipsis), and whether tooltip is required.
3. **New entry-block component:** If the project has no existing component suitable for a solid rectangular calendar block with label and colour, **STOP** and list here; do not invent a new component without approval.
