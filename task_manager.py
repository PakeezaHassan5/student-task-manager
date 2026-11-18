"""Core logic for the Student Task Manager."""


class Task:
    """Represents a single task."""

    def __init__(self, task_id, title, completed=False):
        self.task_id = task_id
        self.title = title
        self.completed = completed

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{self.task_id}. {status} {self.title}"


class TaskManager:
    """Stores tasks in memory and provides operations on them."""

    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
        """Create a new task. Empty titles are rejected."""
        if title is None or not title.strip():
            raise ValueError("Task title cannot be empty.")
        task = Task(self._next_id, title.strip())
        self.tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self):
        """Return a copy of the task list."""
        return list(self.tasks)

    def complete_task(self, task_id):
        """Mark the task with the given ID as completed."""
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive whole number.")
        for task in self.tasks:
            if task.task_id == task_id:
                if task.completed:
                    return False  # already completed
                task.completed = True
                return True
        return False

    def summary(self):
        """Return (total, completed, pending) counts."""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.completed)
        return total, completed, total - completed

    def delete_task(self, task_id):
        """Delete the task with the given ID."""
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive whole number.")
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return True
        return False