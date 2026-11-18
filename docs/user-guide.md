# User Guide - Student Task Manager

## Starting the program

Open a terminal in the project folder and run:

    python main.py

## Menu options

| Option | Action |
|--------|--------|
| 1 | Add a task. Type a title. Empty titles are rejected. |
| 2 | Display all tasks. [ ] means pending, [x] means completed. |
| 3 | Complete tasks. Enter one ID or several IDs separated by commas, e.g. 1,3 |
| 4 | Delete a task. Enter the ID shown in the list. |
| 5 | Show how many tasks are total, completed and pending. |
| 6 | Exit the program. |

## Example session

1. Choose 1 and enter "Finish DevOps lab".
2. Choose 1 and enter "Prepare for viva".
3. Choose 2 to see both tasks.
4. Choose 3 and enter 1 to complete the first task.
5. Choose 5 to see the summary: Total 2, Completed 1, Pending 1.

## Common messages

- "Task title cannot be empty." - type at least one visible character.
- "not a valid task ID" - enter a positive whole number from the list.
- "Task not found" - the ID does not exist or was already deleted.

## Note

Tasks are stored in memory only and are cleared when the program exits.