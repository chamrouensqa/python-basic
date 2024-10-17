class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.name} [{status}]"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)
        print(f"Added task: '{task_name}'")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Removed task: '{removed_task.name}'")
        else:
            print("Invalid task index!")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            print(f"Marked task as completed: '{self.tasks[task_index].name}'")
        else:
            print("Invalid task index!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

def main():
    todo_list = ToDoList()
    while True:
        print("\nCommands: add, remove, complete, list, quit")
        command = input("Enter a command: ").strip().lower()

        if command == "add":
            task_name = input("Enter task name: ").strip()
            todo_list.add_task(task_name)

        elif command == "remove":
            try:
                task_index = int(input("Enter task number to remove: ")) - 1
                todo_list.remove_task(task_index)
            except ValueError:
                print("Please enter a valid number.")

        elif command == "complete":
            try:
                task_index = int(input("Enter task number to complete: ")) - 1
                todo_list.complete_task(task_index)
            except ValueError:
                print("Please enter a valid number.")

        elif command == "list":
            todo_list.list_tasks()

        elif command == "quit":
            print("Exiting to-do list.")
            break

        else:
            print("Unknown command. Please try again.")

