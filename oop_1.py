"""
def hello_func():
    print('hello')

print(type(hello_func))

string = 'hello'
print(string.upper())
"""


class Employee:
    
    # instantiates the object immediately with the given parameters
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def add_one(self, x):
        return x + 1
    
    def hello(self):
        print('Hello!')
        
    def set_age(self, age):
        self.age = age


""" an object is an instance of a specific class; the arguments of the objects below will be passed to the 
Employee class to the __int__ function defined that contains the name and age parameters"""
employee_1 = Employee('Marius', 29)
print(employee_1.get_age())

employee_2 = Employee('Paul', 28)
print(employee_2.get_name())

employee_3 = Employee('Melanie', 23)
employee_3.set_age(24)
print(employee_3.get_age())

"""
employee_1.hello()
print(employee_1.add_one(5))
print(type(employee_1))
"""
