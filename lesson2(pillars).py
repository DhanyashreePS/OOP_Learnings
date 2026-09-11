#Pillars of OOP
#abstraction - which hides inner working ,only showing important things

#Encapsulation

'''class ATM:
    def __init__(self,balance):
        self.__balance=balance  #private object you can't externally change balance
    
    def check_bal(self):
        print(self.__balance)
        
atm=ATM(5000)
print(atm.__balance)'''

class Database:
    def __init__(self):
        self.__storage= {}
        
    def write(self, key, value):
        self.__storage[key]=value
    
    def read(self,key):
        if key in self.__storage:
            print(self.__storage[key])
        else:
            print("DB item not available!")
    
db= Database()
db.write("subscribers", "100k")
db.write("name","dhanya")
db.read("name")# output : dhanya

#print(db.__storage)#print(db.__storage) AttributeError: 'Database' object has no attribute '__storage'
#db.storage will give you entire db ,no security change storage to private attribute by __ , for protected _
    