# Calendar Module – Technical Documents Index

**Epic:** Calendar Module (Time Tracker – Nexus)  
**Source of subtasks:** ClickUp task view ([link](https://app.clickup.com/90161493585/v/b/s/90166381031)) and local script `scripts/clickup_create_calendar_subtasks.py`.  
**Note:** The ClickUp web view at the link above was not fully accessible (generic mobile prompt). Subtask names and scope are taken from `scripts/clickup_create_calendar_subtasks.py` and `docs/calendar-module-user-stories.md`, which align with the approved user stories.

---

## Shared reference

| Document | Purpose |
|----------|---------|
| [calendar-module-data-schema.md](calendar-module-data-schema.md) | Single source of truth for data fields and entities. All tech docs reference this; no invention of fields. |

---

## Subtask technical documents (5 only)

| # | Subtask (ClickUp / script) | Technical document |
|---|----------------------------|---------------------|
| 1 | View and navigate calendar | [tech-doc-01-view-and-navigate-calendar.md](tech-doc-01-view-and-navigate-calendar.md) |
| 2 | See entries on calendar | [tech-doc-02-see-entries-on-calendar.md](tech-doc-02-see-entries-on-calendar.md) |
| 3 | Add, view, edit, and delete single entry | [tech-doc-03-add-view-edit-delete-single-entry.md](tech-doc-03-add-view-edit-delete-single-entry.md) |
| 4 | Multi-select, reschedule, and resize entries | [tech-doc-04-multi-select-reschedule-resize-entries.md](tech-doc-04-multi-select-reschedule-resize-entries.md) |
| 5 | Filter and scope | [tech-doc-05-filter-and-scope.md](tech-doc-05-filter-and-scope.md) |

---

## Document structure (per subtask)

Each technical document contains:

- **Scope Boundary** – In/out of scope for that subtask.
- **Frontend Blueprint** – React/UI using existing components only; STOP and list NEEDS CLARIFICATION if a new component is required.
- **Backend Blueprint** – Django/DRF APIs; `core.responses`; no invented endpoints or fields.
- **Data Schema** – Reference to `calendar-module-data-schema.md` plus any subtask-specific notes.
- **NEEDS CLARIFICATION** – Missing story input or required new components; implementation must wait until clarified.

---

## Rules applied

- **ZERO invention** of logic, APIs, fields, or validations.
- **Existing UI components only;** if a new component seems required, STOP and list in NEEDS CLARIFICATION.
- If any story input is missing, STOP and list in NEEDS CLARIFICATION.
