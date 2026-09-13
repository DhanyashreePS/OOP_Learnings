#Abstract class
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Bike(Vehicle):
    def __init__(self,name):
        self.name = name
        
b = Bike("KTM")
print(b.name)
"""

'''b = Bike("KTM")
        ^^^^^^^^^^^
TypeError: Can't instantiate abstract class Bike without an implementation for abstract method 'start_engine'

'''


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Bike(Vehicle):
    def __init__(self,name):
        self.name = name
        
    def start_engine(self):
        print("Bike engine is starting...")  
          
b = Bike("KTM")
print(b.name)
