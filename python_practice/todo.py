class TodoList:
    def __init__(self):
        self.personName = input("What is the Person's name?  ")
        self.task=[]
        self.completed=[]
        print(f"HELLO {self.personName}!!!")

    def AddTask(self):
        task=input(f" So , {self.personName}  Enter you Task  ")
        self.task.append(task)
        print(f"These are you Tasks pending in your Todo list {self.task}")
        print(f"These are you Tasks completed in your Todo list {self.completed}")
    
    def FinishedTask(self):
        finish= input(f"So {self.personName} , What task did u complete?")
        if finish not in self.task:
            print("THIS TASK DOES NOT EXIST")
            finish= input(f"So {self.personName} , What task did u complete?")
        else:
         self.completed.append(finish)
         self.task.remove(finish)
         print(f"These are you Tasks completed in your Todo list {self.completed}")
         print(f"These are you Tasks pending in your Todo list {self.task}")


p1=TodoList()
p1.AddTask()
p1.AddTask()
p1.AddTask()
p1.FinishedTask()
p1.FinishedTask()