# Technical Document: View and Navigate Calendar

**Subtask (from ClickUp):** View and navigate calendar  
**User Story:** Story 1 – View and navigate the calendar  
**Sources:** `calendar-module-requirement-and-ui.md`, `calendar-module-epic.md`, `calendar-module-user-stories.md`  
**Design reference:** Figma 02.1 Time Tracker - Nexus, node 7369-75653 (top bar; calendar grid with day labels).

---

## Scope Boundary

**In scope**

- Month view and Week view selectable via a **segmented control** in the top bar.
- **Previous/Next** arrow buttons flanking the period display (e.g. “October 2024”) to change visible period.
- **“Today”** button to show the period containing the current date.
- **Current day (“Today”)** visually highlighted in the calendar grid.
- **Month view:** Day grid with day-of-week labels (e.g. Mon, Tue); first day of week **Monday**; no week numbers.
- **Week view:** Day columns Monday–Sunday; vertical axis with **hourly time markers** (e.g. 9 AM, 10 AM).

**Out of scope**

- Day view; week numbers; any behaviour not in the Requirement Document.

---

## Frontend Blueprint

- **Top bar (from requirement):** Period label (e.g. “October 2024”), left/right arrows, Month/Week segmented control, “Today” button. No invention of controls.
- **Main area:** Calendar grid (month) or week columns (week). Monday as first day; week view shows hourly axis.
- **Components:** Use **existing UI components only** (segmented control, buttons, calendar grid). If the project has no calendar grid or period-navigation component, **STOP and add to NEEDS CLARIFICATION**.
- **State:** View mode (month | week), current period (date range or month/year), and derived “today” highlight from current date.

---

## Backend Blueprint

- **No new APIs required** for this subtask. View and period are client state; backend only needs to support listing time entries for a given date range (used by “See entries on calendar” and later subtasks).
- If an **existing** endpoint already returns entries for a range, reuse it. Do not invent new endpoints for “view” or “navigate.”

---

## Data Schema

- See **`calendar-module-data-schema.md`**. This subtask does not introduce or change fields.
- Period (month/week range) is derived on the frontend; any list endpoint used for entries should accept **date-range** (or equivalent) query parameters as defined in the schema/API contract for entries.

---

## NEEDS CLARIFICATION

- None for this subtask if existing UI components exist for: segmented control, period display, previous/next, Today, and month/week grid with Monday start and hourly axis.
- If **no existing calendar or period-navigation component** exists: list the required component(s) here and do not implement until clarified.
