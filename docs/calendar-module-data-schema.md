# Calendar Module – Data Schema (Reference)

**Purpose:** Single source of truth for calendar/time-entry data. All technical docs reference this; no invention of fields beyond the Requirement Document.

**Sources:** `calendar-module-requirement-and-ui.md`, `calendar-module-epic.md`, `calendar-module-user-stories.md`.

---

## Entities implied by requirement (WHAT only)

- **Time entry:** Represents one block on the calendar. Requirement mentions: Task Name, Project, Time (and “any others shown in the final design”). Entries have types or statuses distinguished by colour; can span one or more time slots or days in week view.
- **Filter dimensions:** Project, Task, User (each with “Select All” and individual checkboxes).
- **Calendar scope:** Configurable (e.g. personal, team-wide); exact options “as configured.”

## Fields (from requirement only – no invention)

| Concept        | Source in requirement                         | Notes |
|----------------|------------------------------------------------|-------|
| Task name      | Edit Entry modal: “Task Name”                  | Label on block = e.g. task or project name. |
| Project        | Edit Entry modal: “Project”; filter “Project”  | One project per entry for filtering/display. |
| Time           | Edit Entry modal: “Time”; resize = duration    | Start and duration (or start/end) required for placement and resize. Exact semantics per product. |
| Entry type/status | “Distinguished by colour”                    | **NEEDS CLARIFICATION:** Which types/statuses and how many colours not defined. |
| User           | Filter “User”; scope “personal” vs “team-wide”  | Entries are attributable to a user for filtering and scope. |

## Database / API shape (minimal)

- Backend **MUST NOT** add fields not listed above or agreed in NEEDS CLARIFICATION.
- Primary resource: **time entries** (list, create, retrieve, update, delete).
- Filtering: by **project**, **task**, **user** (and scope) as per requirement.
- Response format: project standard `success_response` / `error_response` from `core.responses`.

---

*This file is referenced by all subtask technical documents. Any new field or validation must be added here only after product/requirement clarification.*
