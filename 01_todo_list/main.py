from todo.tasks import ToDoList

def main():
    todo = ToDoList()
    while True:
        print("\n1. Add Tasks")
        print("2. Remove Tasks")
        print("3. View Taska")
        print("4. Exit")

        choice = input("Enter your Choice: ")
        if choice == "1":
            task_name = input("enter task name to be added")
            todo.addTasks(task_name)
        elif choice == "2":
            task_name = input("enter task name to be deleted")
            todo.deleteTasks(task_name)
        elif choice == "3":
            todo.viewTasks()

        elif choice == "4":
            print("Good Bye .....")
            break
        else:
            print("invalid input try again...")

if __name__ == "__main__":
    main()


        

