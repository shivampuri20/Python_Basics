class Employee:
    no_of_emp=0
    raise_amt=1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

    @classmethod                        # A class method gets the class (we usually call it cls ) as the implicit first argument
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount
    
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod                
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)   #calling class method

print emp_1.raise_amt


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')     #parsing the strings

#new_emp_1 = Employee(first, last, pay)
#new_emp_1 = Employee.from_string(emp_str_1)

#print new_emp_1.email
#print new_emp_1.pay


import datetime
my_date = datetime.date(2016, 7, 11)

print Employee.is_workday(my_date)








  
