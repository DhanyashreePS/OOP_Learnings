#Overriding

"""
class Animal:
    def make_sound(self):
        print("Animal is making sound")
    
class Dog(Animal):
    pass
d = Dog()
d.make_sound()

'''o/p: Animal is making sound'''
"""

class Animal:
    def make_sound(self):
        print("Animal is making sound")
    
class Dog(Animal):
    def __init__(self,name):
        self.name = name 
        
    def make_sound(self):
        print(f"{self.name} Barking....")
        
d = Dog()
d.make_sound()

#o/p : Barking...



#super()

"""class Animal:
    def make_sound(self):
        print("Animal is making sound")
    
class Dog(Animal):
    def __init__(self,name):
        self.name = name 
        
    def make_sound(self):
        super().make_sound()
        print(f"{self.name} Barking....")
        
    def angry(self):
        self.make_sound
        
d = Dog("Beat")
d.make_sound()
'''o/p:
Animal is making sound
Barking....
'''
"""


