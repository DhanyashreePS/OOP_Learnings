#Method Overloading
'''class Calculator:
    def add(self, a, b):
        print(a+b)
    
    def add(self, a, b,c):
        print(a+b+c)


c=Calculator()
c.add(1,2)
c.add(1,2,3)
'''

""" Traceback (most recent call last):
    c.add(1,2)
TypeError: Calculator.add() missing 1 required positional argument: 'c'

"""


class Calculator:
    
    def add(self, a, b,c=0): #default parameter
        print(a+b+c)
#o/p :3 and  6

c=Calculator()
c.add(1,2)
c.add(1,2,3)

#Python doesn't support method overloading directly , achieving it through default values or *args nad **kwargs