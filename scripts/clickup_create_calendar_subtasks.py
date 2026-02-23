#!/usr/bin/env python3
"""
Create Calendar Module subtasks under existing ClickUp task 86d227uth.
Requires CLICKUP_API_KEY in environment. Fetches list_id from parent task.
"""

from __future__ import annotations

import os
import sys
from typing import Any

import requests

PARENT_TASK_ID = "86d227uth"
FIGMA_LINK = "https://www.figma.com/design/4Qf2rnpZ0qrOpR6vilPUQ3/" "02.1-Time-Tracker---Nexus?node-id=7369-75653"

SUBTASKS = [
    {
        "name": "View and navigate calendar",
        "description": """As a **user**, I want to **switch between Month and Week views and move between periods**, so that **I can browse my time entries across the calendar**.

**Design reference:** [Calendar Entries – Nexus]({figma})

**Acceptance criteria (Given/When/Then):**
- **Given** I am on the calendar, **When** I use the segmented control in the top bar, **Then** I can select Month view or Week view.
- **Given** I am on the calendar, **When** I click the left/right arrows flanking the period label, **Then** the visible period changes (e.g. previous/next month or week).
- **Given** I am on the calendar, **When** I click "Today", **Then** the calendar shows the period containing the current date.
- **Given** I am viewing the calendar, **When** it is the current day, **Then** that day is visually highlighted in the grid.""".format(
            figma=FIGMA_LINK
        ),
    },
    {
        "name": "See entries on calendar",
        "description": """As a **user**, I want to **see time entries as blocks on the calendar with labels and colours**, so that **I can quickly understand what is scheduled**.

**Design reference:** [Calendar Entries – Nexus]({figma})

**Acceptance criteria (Given/When/Then):**
- **Given** I have time entries, **When** I view Month or Week, **Then** each entry appears as a solid rectangular block in the grid (month) or in day columns (week).
- **Given** entries have types or statuses, **When** I view the calendar, **Then** they are distinguished by colour.
- **Given** an entry has a task or project name, **When** I view the block, **Then** a label is shown with truncation per best practice.
- **Given** I am in Week view, **When** I look at the vertical axis, **Then** hourly time markers (e.g. 9 AM, 10 AM) are shown; entries can span one or more time slots or days.""".format(
            figma=FIGMA_LINK
        ),
    },
    {
        "name": "Add, view, edit, and delete single entry",
        "description": """As a **user**, I want to **add a new entry and view, edit, or delete a single entry**, so that **I can manage my time entries from the calendar**.

**Design reference:** [Calendar Entries – Nexus]({figma})

**Acceptance criteria (Given/When/Then):**
- **Given** I am on the calendar, **When** I click "Add Entry" in the top bar or interact with a selected date/time slot, **Then** I can add a new entry (e.g. via pop-up).
- **Given** I click an entry, **When** the pop-up opens, **Then** I see "Edit" and "Delete" options.
- **Given** I click "Edit", **When** the Edit Entry modal opens, **Then** I see fields (e.g. Task Name, Project, Time) and "Cancel" / "Save".
- **Given** I confirm delete from the entry pop-up, **Then** the entry is removed from the calendar.""".format(
            figma=FIGMA_LINK
        ),
    },
    {
        "name": "Multi-select, reschedule, and resize entries",
        "description": """As a **user**, I want to **select multiple entries and reschedule, resize, or duplicate them**, so that **I can batch actions and adjust times efficiently**.

**Design reference:** [Calendar Entries – Nexus]({figma})

**Acceptance criteria (Given/When/Then):**
- **Given** I select multiple entries, **When** the selection is active, **Then** a floating toolbar offers Delete and Duplicate.
- **Given** I drag an entry to another date/time, **When** I drop it, **Then** the entry is rescheduled.
- **Given** I am in Week view, **When** I use the bottom handle on an entry, **Then** I can resize the entry to adjust duration.
- **Given** a Project Tasks list (e.g. left panel) is in scope, **When** I drag a task onto the calendar, **Then** an entry is created or assigned.""".format(
            figma=FIGMA_LINK
        ),
    },
    {
        "name": "Filter and scope",
        "description": """As a **user**, I want to **filter entries by Project, Task, and User and set calendar scope**, so that **I see only relevant entries (e.g. personal vs team)**.

**Design reference:** [Calendar Entries – Nexus]({figma})

**Acceptance criteria (Given/When/Then):**
- **Given** I open the Filters panel from the top bar, **When** it is open, **Then** I see Project, Task, and User filters with "Select All" and individual checkboxes.
- **Given** I change filter selections, **When** I apply them, **Then** the calendar shows only entries matching the filters.
- **Given** calendar scope is configurable, **When** I set scope (e.g. personal, team-wide), **Then** the calendar reflects the chosen scope.""".format(
            figma=FIGMA_LINK
        ),
    },
]


def get_auth_headers(api_key: str) -> dict[str, str]:
    return {"Authorization": api_key, "Content-Type": "application/json"}


def get_parent_task(api_key: str) -> dict[str, Any]:
    url = f"https://api.clickup.com/api/v2/task/{PARENT_TASK_ID}"
    resp = requests.get(url, headers=get_auth_headers(api_key), timeout=30)
    resp.raise_for_status()
    return resp.json()


def create_subtask(api_key: str, list_id: str, name: str, description: str) -> dict[str, Any]:
    url = f"https://api.clickup.com/api/v2/list/{list_id}/task"
    payload = {
        "name": name,
        "description": description,
        "parent": PARENT_TASK_ID,
    }
    resp = requests.post(url, headers=get_auth_headers(api_key), json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()


def main() -> int:
    api_key = os.environ.get("CLICKUP_API_KEY") or os.environ.get("CLICKUP_TOKEN")
    if not api_key:
        print(
            "Set CLICKUP_API_KEY (or CLICKUP_TOKEN) with your ClickUp API key.",
            file=sys.stderr,
        )
        return 1
    parent = get_parent_task(api_key)
    list_id = parent.get("list", {}).get("id")
    if not list_id:
        print("Could not determine list_id from parent task.", file=sys.stderr)
        return 1
    print(f"Parent task list_id: {list_id}")
    created = []
    for st in SUBTASKS:
        try:
            task = create_subtask(api_key, str(list_id), st["name"], st["description"])
            task_id = task.get("id")
            created.append((st["name"], task_id))
            print(f"Created subtask: {st['name']} -> {task_id}")
        except requests.HTTPError as e:
            print(f"Failed to create '{st['name']}': {e}", file=sys.stderr)
    if created:
        print("\nCreated subtasks:")
        for name, tid in created:
            print(f"  - {name}: https://app.clickup.com/t/{tid}")
    return 0 if len(created) == len(SUBTASKS) else 1


if __name__ == "__main__":
    sys.exit(main())
