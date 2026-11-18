"""Console interface for the Student Task Manager."""

from task_manager import TaskManager
def add_task_ui(manager):
    title = input("Enter task title: ")
    task = manager.add_task(title)
    print(f"Task added: {task}")

def display_tasks_ui(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(task)
def complete_task_ui(manager):
    task_id = int(input("Enter task ID to complete: "))
    if manager.complete_task(task_id):
        print("Task marked as completed.")
    else:
        print("Task not found.")
def print_summary_ui(manager):
    total, completed, pending = manager.summary()
    print(f"Total: {total} | Completed: {completed} | Pending: {pending}")
def delete_task_ui(manager):
    task_id = int(input("Enter task ID to delete: "))
    if manager.delete_task(task_id):
        print("Task deleted.")
    else:
        print("Task not found.")
def print_menu():
    print("\n===== Student Task Manager =====")
    print("1. Add task")
    print("2. Display tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Show summary")
    print("6. Exit")
def main():
    manager = TaskManager()
    actions = {
        "1": add_task_ui,
        "2": display_tasks_ui,
        "3": complete_task_ui,
        "4": delete_task_ui,
        "5": print_summary_ui,
    }
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(manager)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()