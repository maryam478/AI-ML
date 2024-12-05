class Person:
    def __init__(self,name,age,location):
        self.name=name
        self.age=age
        self.location=location
    
    def greet(self,compliment):
        self.compliment=compliment
        print(f"Hello my name is {self.name}, I am {self.age} years old and I am from {self.location}")
    def comp(self):
        print(f" you are {self.compliment}")

p1=Person('Emma',25,'New York')
p1.greet('beautiful')
p1.comp()