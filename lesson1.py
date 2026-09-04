class Human:
    def __init__(self,name, age):
        print("Const called by: ",name)
        self.name=name
        self.age=age
        
    def walk(self):
        print(f'{self.name} is walking')

#Init for just passing value directly to class
d=Human("Dhanya",20)
p=Human("Preeti",22)
d.walk()

