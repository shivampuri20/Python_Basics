#inheritance
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


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay,prog_lang,employees=None):
        super().__init__ (first,last,pay)

        if employees is None:
            self.employees=[]
        else:
            self.employees=employees


    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        print 'emp.fullname()'

emp_1 = Developer('Corey', 'Schafer', 50000,'python')
emp_2 =  Developer('Test', 'Employee', 60000,'java')

#mgr1=Manager('sue','smith',90000,[emp_1])
#print mgr1.email

mgr1.add_emp(emp_2)

#print emp_1.email
#print emp_1.prog_lang


#print emp_1.pay
#emp_1.apply_raise()
#print emp_1.pay

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()




