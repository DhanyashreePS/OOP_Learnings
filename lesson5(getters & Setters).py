#oveloading/overriding/ Getters/ Setters
#Getters and Setters
"""class Student:
    def __init__(self,name,age):
        self.age=age
        
s=Student("Dhanya",'20')
s.age='15'   #Any one can modify any time ,no controlled access
print(s.age)"""


class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        
    def get_name(self):   #Getter method
        return self.__name #o/p: Dhanya (we can access private attributes using Getter method)
    
    def set_name(self, name):  #Setter method
        self.__name = name
        
    def set_age(self, age):
        if isinstance(age , int):
            self.__age = age
            print(self.__age)
        else:
            print("ERROR")
        
s=Student("Dhanya",'20')   
print(s.get_name())

s.set_name("Anki")
print(s.get_name()) 
'''
o/p: 
Dhanya 
Anki 
'''

s.set_age(25)
s.set_age("ab")
'''
o/p:
Dhanya
Anki
25
ERROR
'''



        