# practice 3/18/25
# chapter 11 - employee
# employee_11_3.py

class Employee:
    '''A class to model employee info such as name, and salary.'''

    def __init__(self, first_name, last_name, salary):
        '''Initialize employee attributes.'''
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, amount=5000):
        self.salary += amount

# fb = Employee('foo', 'bar', 50_000)
# print(f"Employee: {fb.first_name} {fb.last_name}, Salary: ${fb.salary}")
# fb.give_raise()
# print(f"Employee: {fb.first_name} {fb.last_name}, Salary: ${fb.salary}")
# fb.give_raise(10_000)
# print(f"Employee: {fb.first_name} {fb.last_name}, Salary: ${fb.salary}")