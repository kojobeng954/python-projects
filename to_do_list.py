import datetime


def display_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Date: {task['date']}")
        print("-" * 20)


def add_task(tasks):
    task = {
        "title": input("Enter the task title: "),
        "description": input("Enter the task description: "),
        "date": datetime.date.today(),
    }
    tasks.append(task)
    print("Task added successfully.")


def remove_task(tasks):
    title = input("Enter the title of the task to remove: ")
    for task in tasks:
        if task["title"] == title:
            tasks.remove(task)
            print("Task removed successfully.")
            return
    print("Task not found.")


def main():
    tasks = []
    while True:
        print("To-Do List Menu:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
