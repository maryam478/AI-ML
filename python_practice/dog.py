class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
        print(f"{self.name} the {self.breed} is a Loyal Dog.")
    def bark(self):
        print(f"{self.name} barks WOOF WOOF")
    def sit(self):
        print(f"{self.name} SAT after barking")
    
        
p1=Dog('Buddy','Goldenretriever')
p1.bark()
p1.sit()
# p2=Dog('Tommy','Husky')
# p2.bark()
# p2.sit()
