
import random

class Office:
    def __init__(self,name):
        self.name=name
        self.employee=[]

    def new_joinee(self,name,dept,salary):
        self.employee.append({
            'name':name,
            'dept':dept,
            'salary':salary

        })

    def salary_hike(self,name,hike_percent):
        for name1 in self.employee:
          if name1['name'] == name:
             name1['salary'] = name1['salary']*(100+hike_percent)/100
             print(f'This is the increased salary {name1['salary']}')

    def salary_decriment(self,name,amount):
        for name2 in self.employee:
            if name2['name'] == name:
                name2['salary'] = name2['salary'] - amount
                print(f" The current salary of {name2['name']} is {name2['salary']}")

    def luckyDraw(self):
        lucky_employee=random.choice(self.employee)
        lucky_employee['salary'] = lucky_employee['salary']*2
        print(f"CONGRATULATIONS {lucky_employee['name']} your salary has been increased to {lucky_employee['salary']}")

    def gethigestsalary(self):
        name1 = ''
        sal= 0
        for salary1 in self.employee:
            if salary1['salary'] > sal:
                sal=salary1['salary']
                name1=salary1['name']

        print(f"The person with highest salary is {name1} with a salary of {sal}")

    def getlowestsalary(self):
        name1 = ''
        sal= 10000
        for salary1 in self.employee:
            if salary1['salary'] < sal:
                sal=salary1['salary']
                name1=salary1['name']

        print(f"The person with lowest salary is {name1} with a salary of {sal}") 

    def getemployeeInfo(self):
        for emp in self.employee:
            print(f"{emp}")






            # print(name1['name'])


p1=Office('innovapath')
p1.new_joinee('Tom','hr',100)
p1.new_joinee('Srk','sw',700)
p1.new_joinee('Kim','developer',100)
p1.new_joinee('Leo','it',100)
p1.new_joinee('John','hr',150)
p1.salary_hike('Tom',10)
p1.salary_decriment('tom',5)
p1.luckyDraw()
p1.gethigestsalary()
p1.getlowestsalary()
# p1.getemployeeInfo()

        
      