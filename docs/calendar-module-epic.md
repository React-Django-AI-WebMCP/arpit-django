# Epic: Calendar Module (Time Tracker – Nexus)

## Goal

Deliver the Calendar module for Time Tracker (Nexus) so users can view, create, edit, delete, duplicate, filter, and reschedule time entries on a Month or Week calendar with configurable scope (e.g. personal, team-wide) and responsive layout, as defined in the Requirement Document.

---

## In Scope

- **Views and navigation**
  - Month view and Week view, selectable via a segmented control in the top bar.
  - Change visible period via left and right arrow buttons (Previous/Next) flanking the period display (e.g. “October 2024”).
  - “Today” button to return to the current date’s period.
  - Current day (“Today”) visually highlighted in the calendar grid.

- **Entries on calendar**
  - Time entries shown as solid rectangular blocks in the calendar grid (month view) or in day columns (week view).
  - Entry types or statuses distinguished by colour.
  - Labels on blocks (e.g. task or project name); content and truncation per best practice.
  - Week view: hourly time markers on the vertical axis (e.g. 9 AM, 10 AM).
  - Entries can span one or more time slots or days in week view.

- **Selection**
  - Select a single date in month view (circle highlight).
  - In week view, time slots used for placing or moving entries (e.g. add entry, drag).
  - Select multiple entries at once.

- **Actions**
  - Add entry: from “Add Entry” button in top bar or from pop-up when interacting with a selected date or time slot.
  - View entry details: clicking an entry opens a pop-up with “Edit” and “Delete.”
  - Edit entry: from entry pop-up, open “Edit Entry” modal with fields (e.g. Task Name, Project, Time) and “Cancel” / “Save.”
  - Delete entry: from entry pop-up or from floating toolbar when multiple entries selected.
  - Duplicate entry: from floating toolbar when multiple entries selected.
  - Reschedule: entries draggable to change date/time.
  - Adjust duration: in week view, entries resizable (e.g. via bottom handle).
  - Drag from project tasks: support dragging tasks from a “Project Tasks” list (e.g. left panel) onto the calendar to create or assign entries.

- **Filtering**
  - Filter calendar entries by Project, Task, and User.
  - Filters panel with “Select All” and individual checkboxes per filter.

- **Calendar scope**
  - Configurable (e.g. personal, team-wide, or other options as configured).

- **Layout and UI**
  - Top bar: period label, previous/next arrows, Month/Week selector, “Today,” “Filters,” “Add Entry.”
  - Main area: calendar grid (month) or week columns (week).
  - Optional left panel for “Project Tasks” when drag-from-tasks is in scope.
  - Filters panel opens from “Filters” control (top-right).
  - Month view: day grid, day-of-week labels (e.g. Mon, Tue), Monday as first day of week; no week numbers.
  - Week view: day columns (Monday–Sunday), hourly axis.
  - Empty state: central message (e.g. “No entries yet”) and “Add Entry” button.
  - Loading and error states implemented following best practice.

- **Responsive**
  - Layout and behaviour adapt across viewport sizes (e.g. desktop, tablet, mobile).

---

## Out of Scope

- Day view (only Month and Week are in the Requirement Document).
- Any entry types, statuses, or colours not defined in the Requirement Document.
- Week numbers in the calendar (not in design).
- APIs, database design, backend logic, or technical architecture (requirement doc is WHAT only).
- Features or behaviours not stated in the Requirement Document.

---

## NEEDS CLARIFICATION

- **Entry label content and truncation:** Requirement Document defers to “best practice” / implementer’s choice; exact rules (max length, truncation pattern, tooltip) not specified.
- **Loading and error states:** Requirement Document defers to “best practice”; exact copy, placement, and behaviour not specified.
- **Entry types and statuses:** Requirement Document states distinction “by colour” but does not list which entry types or statuses exist or how many colours; needed for consistent UI.
- **“Project Tasks” left panel:** Whether this panel is always visible, only in a specific mode, or configurable (requirement doc says “when … in scope” but does not define when that is).
