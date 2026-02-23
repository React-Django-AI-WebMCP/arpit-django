# Technical Document: Add, View, Edit, and Delete Single Entry

**Subtask (from ClickUp):** Add, view, edit, and delete single entry  
**User Story:** Story 3 – Add, view, edit, and delete a single entry  
**Sources:** `calendar-module-requirement-and-ui.md`, `calendar-module-epic.md`, `calendar-module-user-stories.md`  
**Design reference:** Figma 02.1 Time Tracker - Nexus, node 7369-75653 (Add Entry button, entry pop-up with Edit/Delete, Edit Entry modal).

---

## Scope Boundary

**In scope**

- **Add entry:** From “Add Entry” button in top bar, or from pop-up when user interacts with a selected date (month) or time slot (week).
- **View entry details:** Clicking an entry opens a **pop-up** with “Edit” and “Delete.”
- **Edit entry:** From entry pop-up, open “Edit Entry” **modal** with fields (e.g. Task Name, Project, Time) and “Cancel” / “Save.” Save updates entry and closes modal; Cancel closes without saving.
- **Delete entry:** From entry pop-up; entry is removed (behaviour after delete per design/product).

**Out of scope**

- Multi-select or bulk delete/duplicate (see tech-doc-04). Drag-from–Project Tasks (optional; out of scope until clarified). Any fields not in the requirement (e.g. “any others shown in the final design”) must be clarified before adding.

---

## Frontend Blueprint

- **Add Entry:** Button in top bar; use existing button component. Add-from-date/slot: pop-up from selected date/slot; use existing modal/popover if available.
- **Entry pop-up:** On entry click; contains “Edit” and “Delete” only. Use existing pop-up/modal/dropdown component.
- **Edit Entry modal:** Fields: Task Name, Project, Time (and only others explicitly specified in requirement/design). Buttons: “Cancel”, “Save.” Use existing form + modal components.
- **Validation:** Only validations implied by requirement (e.g. required Task Name, Project, Time if stated). No invented validations.
- If a **new** modal or pop-up pattern is required, **STOP** and add to NEEDS CLARIFICATION.

---

## Backend Blueprint

- **Create:** `POST /api/calendar/entries/` with body containing Task Name, Project, Time (and only other agreed fields). Response: `success_response` with created entry; status 201. Use `core.responses.success_response` / `error_response`.
- **Retrieve one:** `GET /api/calendar/entries/{id}/` for entry details (e.g. for pop-up). Response: single entry object; fields per `calendar-module-data-schema.md`.
- **Update:** `PATCH /api/calendar/entries/{id}/` (or PUT if project standard). Body: editable fields (Task Name, Project, Time, etc.). Response: updated entry.
- **Delete:** `DELETE /api/calendar/entries/{id}/`. Response: 204 No Content or 200 with success payload per project standard.
- **No invention:** No extra query params or response fields beyond schema and project API rules.

---

## Data Schema

- See **`calendar-module-data-schema.md`**. Create/update payload: only Task Name, Project, Time (and any product-agreed fields). Validations only for fields defined in requirement or schema doc.

---

## NEEDS CLARIFICATION

1. **Edit Entry modal fields:** Requirement says “e.g. Task Name, Project, Time” and “any others shown in the final design.” Confirm final field list and required vs optional before implementing.
2. **Post-delete behaviour:** Requirement does not specify (e.g. close pop-up, stay on calendar, toast). Confirm with product/design.
3. **New modal/pop-up component:** If no existing component fits entry pop-up or Edit Entry modal, list required component(s) here and do not implement until clarified.
