class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"description": task, "completed": False})

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else " "
            print(f"{index+1}. [{status}] {task['description']}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task number to mark complete: ")) - 1
            todo_list.mark_task_complete(index)
        elif choice == "3":
            index = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()