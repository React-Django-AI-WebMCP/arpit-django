# Combined Requirement & UI Documentation

**Calendar module – Time Tracker (Nexus)**

**Source:** Figma design [02.1 Time Tracker - Nexus](https://www.figma.com/design/4Qf2rnpZ0qrOpR6vilPUQ3/02.1-Time-Tracker---Nexus?node-id=7369-75653) (node 7369-75653). Design board: “Calendar Entries” (Calendar flow v0.3).

---

## 1. Functional Requirements (WHAT the system must do)

The following describe what the system must do from the user’s perspective. No technical or implementation detail is included.

### 1.1 Date and period

- The system must allow the user to see the calendar in **Month** or **Week** view, selectable via a segmented control in the top bar.
- The system must allow the user to change the visible period using **left and right arrow buttons** (Previous / Next) that flank the current period display (e.g. “October 2024”), and a **“Today”** button to return to the current date’s period.

### 1.2 Time / entries on calendar

- The system must show time-related entries as **solid rectangular blocks** in the calendar grid (month view) or in day columns (week view). Entries represent individual calendar/time entries and may show labels on the block.
- The system must allow the user to distinguish between different entry types or statuses by **colour** (e.g. different colours per type or status).

### 1.3 Selection and actions

- The system must allow the user to **select a single date** in month view (shown with a circle highlight). In week view, time slots are used for placing or moving entries (e.g. by adding an entry or dragging). The system must allow **selecting multiple entries** at once.
- The system must support the following actions:
  - **Add entry:** From an “Add Entry” button in the top bar, or from a pop-up when the user interacts with a selected date or time slot.
  - **View entry details:** Clicking an entry block opens a pop-up with “Edit” and “Delete.”
  - **Edit entry:** From the entry pop-up, opening an “Edit Entry” modal with fields (e.g. Task Name, Project, Time) and “Cancel” / “Save.”
  - **Delete entry:** From the entry pop-up, or from a floating toolbar when multiple entries are selected.
  - **Duplicate entry:** From a floating toolbar when multiple entries are selected.
  - **Reschedule / adjust duration:** Entries must be **draggable** to change date/time and **resizable** in week view (e.g. via a bottom handle) to adjust duration. Entries may span multiple days in week view.
  - **Drag from project tasks:** The system must support **dragging tasks from a “Project Tasks” list** (e.g. in a left panel) onto the calendar to create or assign entries.

### 1.4 Filtering and scope

- The system must allow the user to filter calendar entries by **Project**, **Task**, and **User**. Each filter offers a “Select All” checkbox and individual checkboxes for specific items, within a Filters panel.
- The calendar scope is **configurable** (e.g. personal, team-wide, or other options as configured).

### 1.5 Other behaviors

- The system must show an **empty state** when there are no entries: a central message (e.g. “No entries yet”) and an “Add Entry” button.
- Week view must show **hourly time markers** on the vertical axis (e.g. 9 AM, 10 AM).
- The current day (“Today”) must be **visually highlighted** in the calendar grid.
- The system must show appropriate **loading** and **error** states (implementation to follow best practice).

---

## 2. UI Documentation (WHAT is visible and interactable)

This section describes only what is visible on screen and what the user can interact with. It does not describe APIs, data structures, or implementation.

### 2.1 Layout and navigation

- **Top bar:** Contains the current period label (e.g. “October 2024”), previous/next arrow buttons, Month/Week view selector, “Today” button, “Filters” area, and “Add Entry” button.
- **Main area:** The calendar grid (month view) or week columns (week view) occupies the central content area.
- **Left panel (task-drag flow):** When “Dragging entries through project tasks” is in scope, a vertical list of “Project Tasks” appears on the left; users drag items from this list onto the calendar.
- **Filters panel:** Opens (e.g. from a “Filters” control) and shows filter options; placement is in the top-right area of the calendar context.

### 2.2 Calendar area

- **Month view:** A grid of days with numeric dates. Day-of-week labels (e.g. Mon, Tue) appear at the top. The first day of the week is **Monday**. Week numbers are not shown in the design.
- **Week view:** Vertical columns for each day (Monday–Sunday). The vertical axis shows **hourly markers** (e.g. 9 AM, 10 AM, 11 AM). Entries appear as blocks within the day columns and can span one or more time slots or days.

### 2.3 Period and date controls

- **Period display:** Current month and year (e.g. “October 2024”) are shown in the centre of the top bar.
- **Navigation arrows:** Left (`<`) and right (`>`) buttons are placed to the left and right of the period display.
- **View selector:** A segmented control with **“Month”** and **“Week”** options, to the right of the arrows.
- **“Today” button:** A button labelled “Today” is to the right of the view selector.

### 2.4 Entries and events on the calendar

- **Representation:** Entries are **solid rectangular blocks** on the calendar. Blocks show labels (e.g. task or project name); label content and truncation to follow best practice.
- **Colour:** Different **colours** denote different entry types or statuses.
- **Clickable:** Clicking an entry block opens a pop-up with “Edit” and “Delete.”
- **Drag and resize:** Entries are draggable to reschedule; in week view they are resizable (e.g. via a bottom handle) to change duration.

### 2.5 Actions and buttons

- **“Add Entry”:** Button in the top-right of the calendar header.
- **“Filters”:** Control in the top-right area that opens the Filters panel.
- **Entry pop-up:** Appears on click of an entry; shows “Edit” and “Delete.”
- **Multi-select toolbar:** When multiple entries are selected, a floating toolbar shows “Delete” and “Duplicate.”
- **Add / Edit Entry modal:** “Cancel” and “Save” buttons; fields include Task Name, Project, and Time (and any others shown in the final design).

### 2.6 Filters and options

- **Filters panel:** Title “Filters.” Contains:
  - **Project:** “Select All” checkbox plus individual project checkboxes.
  - **Task:** “Select All” checkbox plus individual task checkboxes.
  - **User:** “Select All” checkbox plus individual user checkboxes.
- **View selector:** Segmented control “Month” | “Week” in the top bar (see 2.3).

### 2.7 Empty and other states

- **Empty state:** When there are no entries, the calendar shows a central message (e.g. “No entries yet”) and an “Add Entry” button.
- **Loading and error states:** To be implemented following best practice (copy and placement at implementer’s discretion).

### 2.8 Responsive / variants

- The calendar must be **responsive**: layout and behaviour must adapt appropriately across viewport sizes (e.g. desktop, tablet, mobile).

---

## 3. Unknowns and clarifications list

All previously listed items have been clarified. Summary of decisions:

- **Entry types/statuses:** Distinguished by **colours**.
- **Today highlight:** **Yes** — the current date is visually highlighted in the grid.
- **Calendar scope:** **Configurable** (e.g. personal, team-wide).
- **Entry label copy and truncation:** **Best practice** (implementer’s choice).
- **Loading and error states:** **Best practice** (implementer’s choice).
- **Responsive behaviour:** **Responsive** — layout and behaviour must adapt across viewport sizes.
