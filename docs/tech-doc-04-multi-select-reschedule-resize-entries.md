# Technical Document: Multi-Select, Reschedule, and Resize Entries

**Subtask (from ClickUp):** Multi-select, reschedule, and resize entries  
**User Story:** Story 4 – Multi-select entries and reschedule or resize  
**Sources:** `calendar-module-requirement-and-ui.md`, `calendar-module-epic.md`, `calendar-module-user-stories.md`  
**Design reference:** Figma 02.1 Time Tracker - Nexus, node 7369-75653 (multi-select, floating toolbar, drag/resize).

---

## Scope Boundary

**In scope**

- **Single-date selection (month view):** Select a single date; show with **circle highlight**.
- **Multi-select entries:** Select multiple entries; show **floating toolbar** with “Delete” and “Duplicate.” Delete removes selected entries; Duplicate creates copies (placement per design).
- **Reschedule:** Entry is **draggable** to another date or time slot; on drop, entry date/time is updated.
- **Resize (week view):** Resize control (e.g. **bottom handle**); entry duration changes and block spans new time range.
- **Drag from Project Tasks** is **not** in this doc’s scope; see NEEDS CLARIFICATION below.

**Out of scope**

- Drag-from–Project Tasks behaviour (optional; when/if in scope is undefined in requirement). Any drag/resize behaviour not described in requirement.

---

## Frontend Blueprint

- **Date selection (month):** Single date select with circle highlight; use existing date cell or calendar component if available.
- **Entry multi-select:** Select one or more entry blocks; use existing selection pattern (e.g. checkboxes, shift-click, ctrl-click) if defined; otherwise **NEEDS CLARIFICATION** for interaction.
- **Floating toolbar:** Visible when multiple entries selected; actions “Delete” and “Duplicate” only. Use existing floating toolbar or bar component; if none, **NEEDS CLARIFICATION**.
- **Drag to reschedule:** Entries draggable; drop target = date/time slot. Use existing drag-and-drop or calendar drag support; if new behaviour required, **NEEDS CLARIFICATION**.
- **Resize handle (week view):** Bottom handle to change duration; use existing resize handle or similar; if new component, **NEEDS CLARIFICATION**.
- **APIs:** Call PATCH for reschedule (date/time/duration) and DELETE for delete; duplicate = POST with copied payload (placement rules per design).

---

## Backend Blueprint

- **Update (reschedule):** `PATCH /api/calendar/entries/{id}/` with date/time/duration fields only. Same endpoint as single-entry edit; no new endpoint. Validation: only for fields in schema.
- **Delete:** `DELETE /api/calendar/entries/{id}/`. Bulk delete: either multiple `DELETE` calls or a single **agreed** bulk endpoint (e.g. `POST /api/calendar/entries/bulk-delete/` with list of ids). Do **not** invent bulk endpoint unless product agrees; otherwise document in NEEDS CLARIFICATION.
- **Duplicate:** Create one or more copies. Option A: client calls `POST /api/calendar/entries/` per copy with copied fields (+ new date/time if placement defined). Option B: agreed `POST /api/calendar/entries/{id}/duplicate/` returning new entry. **No invention;** choose per product/backend contract and document.
- Response format: `core.responses` only.

---

## Data Schema

- See **`calendar-module-data-schema.md`**. Reschedule/resize only change Time (start/duration or start/end). Duplicate copies all fields from schema; new id and optionally new date/time per placement rules.

---

## NEEDS CLARIFICATION

1. **Duplicate placement:** Requirement says “placement per design.” Define: same day, same time, or user-chosen? If backend supports a duplicate endpoint, confirm contract.
2. **Bulk delete:** One call per entry vs single bulk-delete endpoint; confirm with product/backend.
3. **Floating toolbar / resize handle / drag-and-drop:** If existing UI components do not support these, list required components and do not implement until clarified.
4. **Drag from Project Tasks:** Requirement says “when … in scope” but does not define when the Project Tasks panel is visible or how drag-from-tasks works. Do not implement until clarified (panel visibility, source API, drop behaviour).
