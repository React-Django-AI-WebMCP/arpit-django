# ClickUp: FE / BE / DB subtasks (MCP spec)

**Use with ClickUp MCP** `create_task` tool to create these 3 subtasks under the user story.

- **Parent task ID:** `86d2280dw`  
- **Parent task:** [View calendar and navigate period](https://app.clickup.com/t/86d2280dw)  
- **List ID:** `901613638985` (same list as parent)

**Reference:** Technical docs `docs/tech-doc-01-view-and-navigate-calendar.md` (and index), `calendar-module-data-schema.md`. Max 3 subtasks: [FE], [BE], [DB]. Not per component or page.

---

## 1. [FE] Frontend Assembly

**name:** `[FE] Frontend Assembly`

**description:**
```markdown
**Scope:** All calendar UI per technical documents. Use existing UI components only.

**Reference:** docs/calendar-module-technical-docs-index.md, tech-doc-01..05, calendar-module-data-schema.md

**In scope:**
- Top bar: period label, prev/next arrows, Month/Week segmented control, Today, Filters, Add Entry.
- Calendar grid (month) and week columns (week); Monday first; hourly axis in week view; today highlight.
- Entry blocks (solid rectangles, labels, colours by type/status); empty state.
- Entry pop-up (Edit, Delete); Edit Entry modal (Task Name, Project, Time; Cancel/Save).
- Multi-select; floating toolbar (Delete, Duplicate); drag to reschedule; resize handle in week view.
- Filters panel (Project, Task, User — Select All + checkboxes); scope selector.
- Responsive layout.

**Design:** [Calendar Entries – Nexus](https://www.figma.com/design/4Qf2rnpZ0qrOpR6vilPUQ3/02.1-Time-Tracker---Nexus?node-id=7369-75653)

**Rules:** No new components without NEEDS CLARIFICATION. Follow tech-doc Scope Boundary and Frontend Blueprint.
```

**MCP call (when `create_task` is available):**
- `list_id`: `901613638985`
- `name`: `[FE] Frontend Assembly`
- `description`: (above)
- `parent`: `86d2280dw`

---

## 2. [BE] Backend Implementation

**name:** `[BE] Backend Implementation`

**description:**
```markdown
**Scope:** All calendar/time-entry APIs per technical documents. Use core.responses only.

**Reference:** docs/calendar-module-technical-docs-index.md, tech-doc-01..05, calendar-module-data-schema.md

**In scope:**
- List entries: `GET /api/calendar/entries/` with query params: date range, project, task, user, scope.
- Create: `POST /api/calendar/entries/` (Task Name, Project, Time; schema only).
- Retrieve: `GET /api/calendar/entries/{id}/`.
- Update: `PATCH /api/calendar/entries/{id}/` (edit + reschedule/resize).
- Delete: `DELETE /api/calendar/entries/{id}/`.
- Optional: bulk delete / duplicate endpoint per tech-doc-04 NEEDS CLARIFICATION.
- Filter-options or use existing project/task/user APIs per tech-doc-05.
- Response format: success_response / error_response; no invented fields.

**Rules:** No invented endpoints or validations. Follow Backend Blueprint in each tech-doc.
```

**MCP call:**
- `list_id`: `901613638985`
- `name`: `[BE] Backend Implementation`
- `description`: (above)
- `parent`: `86d2280dw`

---

## 3. [DB] Schema Changes

**name:** `[DB] Schema Changes`

**description:**
```markdown
**Scope:** Database schema for calendar/time entries only when required by BE.

**Reference:** docs/calendar-module-technical-docs-index.md, tech-doc-01..05, calendar-module-data-schema.md

**In scope (requirement-only fields):**
- Time entry model: task name, project, time (start/duration or start/end), entry type/status (for colour), user (for filter/scope). Use core base models (e.g. TimeStampedModel) if applicable.
- Indexes for list/filter queries (date range, project, task, user).
- Migrations for new/modified tables. No extra fields beyond data-schema doc.

**Rules:** Schema MUST NOT add fields not in calendar-module-data-schema.md or agreed in NEEDS CLARIFICATION.
```

**MCP call:**
- `list_id`: `901613638985`
- `name`: `[DB] Schema Changes`
- `description`: (above)
- `parent`: `86d2280dw`

---

## How to create via MCP

1. Ensure the **ClickUp MCP** server is connected and exposes **create_task** (e.g. project MCP `user-ClickUp` or global `ClickUp` in `.cursor/mcp.json`).
2. For each of the 3 subtasks above, call **create_task** with:
   - `list_id`: `901613638985`
   - `name`: as above
   - `description`: copy the markdown block for that subtask
   - `parent`: `86d2280dw`
3. If your client uses different parameter names (e.g. `listId`), adapt accordingly.
