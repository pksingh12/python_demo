class ToDoList:
    def __init__(self):
        self.tasks = []

    def addTasks(self,task_name):
        self.tasks.append(task_name)
        print(f"Task {task_name} added successfully")

    def deleteTasks(self,task_name):
        if task_name in self.tasks:
            self.tasks.remove(task_name)
            print(f"Task {task_name} removed successfully")
        else:
            print(f"Task {task_name} doese not exist")
    
    def viewTasks(self):
        if not self.tasks:
            print("Task does not exist")
        else:
            for i,j in enumerate(self.tasks,1):
                print(f"{i}. {j}")
