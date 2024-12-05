class Car:
    def __init__(self,carname,model,speed):
        self.carname = carname
        self.model = model
        self.speed = speed
        print(f"The starting speed of {self.carname} {self.model} is {self.speed} Km/hr" )
    def accelarate(self):
            self.speed=self.speed+20
            print(f"{self.carname} {self.model} is running at a speed of {self.speed} Km/hr" )
    def breaking(self):
            self.speed=self.speed-10
            print(f"{self.carname} {self.model} is decreased to speed  {self.speed} Km/hr")


p1= Car('Toyota','Camry',0)
p1.accelarate()
p1.accelarate()
p1.accelarate()
p1.breaking()
        