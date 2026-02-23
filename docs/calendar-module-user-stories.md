# Calendar Module – User Stories (INVEST)

**Epic:** Calendar Module (Time Tracker – Nexus)  
**Source:** Requirement Document (`calendar-module-requirement-and-ui.md`) and Epic (`calendar-module-epic.md`)  
**Design Reference:** Figma [02.1 Time Tracker - Nexus](https://www.figma.com/design/4Qf2rnpZ0qrOpR6vilPUQ3/02.1-Time-Tracker---Nexus?node-id=7369-75653) — node `7369-75653`, board “Calendar Entries” (Calendar flow v0.3).

---

## Story 1: View and navigate the calendar

**As a** user of the Time Tracker (Nexus),  
**I want** to switch between Month and Week view, change the visible period with previous/next arrows and a “Today” button, and see the current day highlighted,  
**so that** I can move through time and focus on the timeframe I need.

**Design Reference:** Figma 02.1 Time Tracker - Nexus, node 7369-75653 (top bar: period label, arrows, Month/Week selector, Today button; calendar grid with day labels).

**Acceptance Criteria**

| Given | When | Then |
|-------|------|------|
| I am on the Calendar module | I use the segmented control in the top bar | The view switches to Month or Week as selected. |
| I am viewing any period | I click the left (previous) or right (next) arrow flanking the period label | The visible period changes to the previous or next month/week. |
| I am viewing a period that is not the current one | I click the “Today” button | The calendar shows the current date’s period (month or week). |
| I am viewing the calendar in month or week view | The current date is in the visible range | The current day (“Today”) is visually highlighted in the grid. |
| I am in week view | I look at the calendar | Day columns show Monday–Sunday; the vertical axis shows hourly time markers (e.g. 9 AM, 10 AM). |
| I am in month view | I look at the calendar | The grid shows days with day-of-week labels (e.g. Mon, Tue); the first day of the week is Monday; week numbers are not shown. |

---

## Story 2: See time entries on the calendar

**As a** user of the Time Tracker (Nexus),  
**I want** to see time entries as solid rectangular blocks with labels and distinct colours for types/statuses (and an empty state when there are no entries),  
**so that** I can understand at a glance what is scheduled and distinguish entry types.

**Design Reference:** Figma 02.1 Time Tracker - Nexus, node 7369-75653 (entry blocks, labels, colours; empty state).

**Acceptance Criteria**

| Given | When | Then |
|-------|------|------|
| I have one or more time entries in the visible period | I view the calendar in Month or Week view | Entries appear as solid rectangular blocks in the grid (month) or in day columns (week). |
| Entries are displayed | I look at the blocks | Each block shows a label (e.g. task or project name); entry types or statuses are distinguished by colour. |
| **NEEDS CLARIFICATION** | — | Exact label content and truncation rules (max length, truncation pattern, tooltip) are not specified in the Requirement Document; implementer follows best practice. |
| **NEEDS CLARIFICATION** | — | Which entry types/statuses and how many colours are not defined in the Requirement Document; needed for consistent UI. |
| There are no entries in the visible period | I view the calendar | An empty state is shown: a central message (e.g. “No entries yet”) and an “Add Entry” button. |
| I am in week view | I look at entries | Entries can span one or more time slots or days. |

---

## Story 3: Add, view, edit, and delete a single entry

**As a** user of the Time Tracker (Nexus),  
**I want** to add an entry (from the top bar or from a selected date/time slot), open an entry to see details, and edit or delete it from the entry pop-up,  
**so that** I can create and maintain my time entries.

**Design Reference:** Figma 02.1 Time Tracker - Nexus, node 7369-75653 (Add Entry button, entry pop-up with Edit/Delete, Edit Entry modal).

**Acceptance Criteria**

| Given | When | Then |
|-------|------|------|
| I am on the calendar | I click “Add Entry” in the top bar | I can create a new entry (e.g. via a modal or flow as per design). |
| I am on the calendar and have selected a date (month) or time slot (week) | I use the add-entry action from that selection (e.g. pop-up) | I can create a new entry for that date/time. |
| An entry exists on the calendar | I click the entry block | A pop-up opens with “Edit” and “Delete.” |
| The entry pop-up is open | I click “Edit” | An “Edit Entry” modal opens with fields (e.g. Task Name, Project, Time) and “Cancel” / “Save.” |
| I am in the Edit Entry modal | I change fields and click “Save” | The entry is updated and the modal closes. |
| I am in the Edit Entry modal | I click “Cancel” | The modal closes without saving changes. |
| The entry pop-up is open | I click “Delete” | The entry is deleted (behaviour after delete per design/product; e.g. pop-up closes). |

---

## Story 4: Multi-select entries and reschedule or resize

**As a** user of the Time Tracker (Nexus),  
**I want** to select multiple entries, use a floating toolbar to delete or duplicate them, and drag or resize entries to reschedule or change duration,  
**so that** I can reorganise and copy time entries quickly.

**Design Reference:** Figma 02.1 Time Tracker - Nexus, node 7369-75653 (multi-select, floating toolbar, drag/resize).

**Acceptance Criteria**

| Given | When | Then |
|-------|------|------|
| I am on the calendar with at least one entry | I select a single date in month view | That date is shown with a circle highlight. |
| There are multiple entries on the calendar | I select more than one entry | Multiple entries are selected and a floating toolbar appears. |
| The floating toolbar is visible (multi-select) | I use the toolbar | “Delete” and “Duplicate” actions are available; Delete removes the selected entries; Duplicate creates copies (placement per design). |
| An entry exists on the calendar | I drag the entry to another date or time slot | The entry is rescheduled (date/time updated). |
| I am in week view and an entry is visible | I use the resize control (e.g. bottom handle) | The entry’s duration changes; the block updates to span the new time range. |

---

## Story 5: Filter entries and set calendar scope

**As a** user of the Time Tracker (Nexus),  
**I want** to open a Filters panel and filter by Project, Task, and User (with “Select All” and per-item checkboxes), and set calendar scope (e.g. personal, team-wide),  
**so that** I see only the entries I care about and the right scope.

**Design Reference:** Figma 02.1 Time Tracker - Nexus, node 7369-75653 (Filters control, Filters panel).

**Acceptance Criteria**

| Given | When | Then |
|-------|------|------|
| I am on the calendar | I click the “Filters” control (top-right area) | The Filters panel opens (e.g. top-right of the calendar context). |
| The Filters panel is open | I look at the options | The panel has title “Filters” and contains: Project (Select All + individual checkboxes), Task (Select All + individual checkboxes), User (Select All + individual checkboxes). |
| I change filter checkboxes (Project, Task, and/or User) | I apply or confirm the filters | The calendar shows only entries that match the selected Project, Task, and User filters. |
| Calendar scope is configurable | I set the scope (e.g. personal, team-wide, or other configured options) | The calendar shows entries according to the selected scope. |

---

## Optional / NEEDS CLARIFICATION

### Drag from Project Tasks

**As a** user of the Time Tracker (Nexus),  
**I want** to drag a task from the “Project Tasks” list (e.g. in a left panel) onto the calendar,  
**so that** I can create or assign a time entry from my task list.

**Design Reference:** Figma 02.1 Time Tracker - Nexus, node 7369-75653 (left panel “Project Tasks”).

**NEEDS CLARIFICATION:** The Requirement Document states this is supported “when … in scope” but does not define when the Project Tasks panel is visible (always, in a specific mode, or configurable). Clarify before implementing.

**Acceptance Criteria (draft)**

| Given | When | Then |
|-------|------|------|
| The Project Tasks panel is visible and in scope | I drag a task from the list onto a date or time slot on the calendar | A new entry is created or assigned for that task at the drop target. |

---

## Cross-cutting (from Requirement Document)

- **Loading and error states:** **NEEDS CLARIFICATION** — Requirement Document defers to “best practice”; exact copy, placement, and behaviour not specified.
- **Responsive:** Layout and behaviour must adapt across viewport sizes (e.g. desktop, tablet, mobile); no additional stories assumed beyond what is in scope above.
