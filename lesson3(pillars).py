# Inheritance and polymorphism
'''class Family:
    def __init__(self,surname):
        self.surname = surname

class Child(Family):
    def __init__(self,name, surname):
        super().__init__(surname)
        self.name = name
        
ch=Child("Dhanya","PS")
print(f"{ch.name} {ch.surname}")''' #Inherits the surname


#Programming example
class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    
    def login(self):
        print(f"{self.username} logged in")
        
class Admin(User):
    def delete_user(self):
        print("Admin deleted the user")

ad= Admin("Dhanya","1243")
ad.login()
print(ad.username)
ad.delete_user()
 
#output 
"""Dhanya logged in
Dhanya
Admin deleted the user"""      