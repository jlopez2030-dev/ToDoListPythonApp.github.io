ToDoList = []
while True:
    print("\n======================")  # Divider
    print("  --- To-Do List ---")
    print("  1. Add Task\n  2. View Tasks\n  3. Remove Task\n  4. Exit")
    print("Notice! The To-Do List's contents will be removed unless the app is still running.")
    print("Choose a category (1-4): ")
    ToDoListCategoryChoice = int(input())

    if ToDoListCategoryChoice == 1:
        print("\n=================")
        Task = input("Enter a new task: ")
        ToDoList.append(Task)
        print(f"Task '{Task}' added!")

    elif ToDoListCategoryChoice == 2:
        if len(ToDoList) == 0:
            print("Your To-Do List is empty.")
        else:
            print("\n======================")
            print("  --- YOUR TASKS ---")
            for i, Task in enumerate(ToDoList):
                print(f"  {i + 1}. {Task}")

    elif ToDoListCategoryChoice == 3:
        if len(ToDoList) == 0:
            print("\nNo tasks to remove.")
        else:
            print("\n=======================")
            print("\n=== REMOVE TASK ===")
            for i, Task in enumerate(ToDoList):
                print(f"{i + 1}. {Task}")

                Index = int(
                    input("\n===============================\nEnter the task number to remove: ")) - 1

                if 0 <= Index < len(ToDoList):
                    Removed = ToDoList.pop(Index)
                    print(f"Removed task: {Removed}")
                else:
                    print("Invalid task number!")

    else:
        break