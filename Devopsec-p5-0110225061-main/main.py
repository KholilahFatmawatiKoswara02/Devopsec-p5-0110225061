from app.task_manager import TaskManager


def main():
    manager = TaskManager()

    while True:
        print("\n=== Student Task Manager ===")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task title: ")

            try:
                task = manager.add_task(title)
                print(f"Task added: {task['title']}")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            for task in manager.list_tasks():
                status = "Done" if task["completed"] else "Pending"
                print(f"{task['id']}. {task['title']} - {status}")

        elif choice == "3":
            try:
                task_id = int(input("Task ID: "))
                task = manager.complete_task(task_id)
                print(f"Completed: {task['title']}")
            except (ValueError, KeyError):
                print("Invalid task ID.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
