class Human:
    def __init__(self,name="Unknowm", age=0, salary=-1):
        print("Const called by: ",name)
        self.name=name #it is instance variable
        self.age=age
        self.salary=salary
        
    def walk(self):
        print(f'{self.name} is walking')

#Init for just passing value directly to class
d=Human("Dhanya",20,50000)
p=Human("Preeti",2)
alice=Human()
d.walk()
alice.walk()

