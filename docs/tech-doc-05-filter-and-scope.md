# Technical Document: Filter and Scope

**Subtask (from ClickUp):** Filter and scope  
**User Story:** Story 5 – Filter entries and set calendar scope  
**Sources:** `calendar-module-requirement-and-ui.md`, `calendar-module-epic.md`, `calendar-module-user-stories.md`  
**Design reference:** Figma 02.1 Time Tracker - Nexus, node 7369-75653 (Filters control, Filters panel).

---

## Scope Boundary

**In scope**

- **Filters control:** In top-right area; opens **Filters panel** (e.g. top-right of calendar context).
- **Filters panel:** Title “Filters.” Contains:
  - **Project:** “Select All” checkbox + individual project checkboxes.
  - **Task:** “Select All” checkbox + individual task checkboxes.
  - **User:** “Select All” checkbox + individual user checkboxes.
- Applying filters: calendar shows **only entries matching** selected Project, Task, and User.
- **Calendar scope:** Configurable (e.g. personal, team-wide, or other configured options); calendar shows entries according to selected scope.

**Out of scope**

- Filter dimensions or scope options not in the requirement. Any filter UI or API not listed above.

---

## Frontend Blueprint

- **Filters control:** Button or control in top bar that opens the panel; use existing trigger component.
- **Filters panel:** Panel with title “Filters” and three sections: Project, Task, User. Each section: “Select All” + list of checkboxes. Use existing panel/drawer and checkbox components only.
- **Scope selector:** Requirement says “configurable (e.g. personal, team-wide).” Use existing selector (dropdown, segmented control, etc.) if available; options only as configured (no invented options). If no existing component, **NEEDS CLARIFICATION**.
- **State:** Selected project ids, task ids, user ids; selected scope. Send to backend as query params or in a single request as per backend contract.

---

## Backend Blueprint

- **List entries** (same as tech-doc-02): `GET /api/calendar/entries/` must support **query parameters** for:
  - **project** (e.g. `project` or `projects`): filter by one or more project ids.
  - **task** (e.g. `task` or `tasks`): filter by one or more task ids.
  - **user** (e.g. `user` or `users`): filter by one or more user ids.
  - **scope** (e.g. `scope=personal` or `scope=team`): filter by calendar scope.
- Parameter names and multi-value format (e.g. `?project=1&project=2` or `?projects=1,2`) per project URL conventions. No extra invented params.
- **Options for filters:** Backend may expose **list of projects**, **list of tasks**, **list of users** (for current user/scope) so the frontend can build “Select All” and per-item checkboxes. Endpoints only if required by UI; e.g. `GET /api/calendar/filter-options/` or existing project/task/user APIs. **Do not invent** new endpoints without product agreement; document in NEEDS CLARIFICATION if needed.
- Response format: `core.responses`; list payload per `calendar-module-data-schema.md`.

---

## Data Schema

- See **`calendar-module-data-schema.md`**. Filter dimensions: Project, Task, User. Scope: configurable options (e.g. personal, team-wide). No new entry fields; only query/scope semantics for listing.

---

## NEEDS CLARIFICATION

1. **Scope options:** Requirement says “e.g. personal, team-wide, or other options as configured.” Confirm full list of scope values and how they map to backend (e.g. single user vs team ids).
2. **Filter options endpoints:** If the frontend needs to populate Project/Task/User checkboxes from the backend, confirm whether to use existing project/task/user APIs or a dedicated calendar filter-options endpoint. No invention of endpoints.
3. **New panel/selector component:** If no existing panel or scope selector fits, list required component(s) and do not implement until clarified.
