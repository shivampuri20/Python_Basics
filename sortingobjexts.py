from operator import attrgetter
class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def __repr__(self):
        return '{},{},${}'.format(self.name,self.age,self.salary)


e1=Employee('carl' ,20,30000)
e2=Employee('dark',30,27678)
e3=Employee('louis',48,654638)

employees=[e1,e2,e3]

def e_sor(emp):
    print emp.name

sorting_emp=sorted(employees,key=e_sor,reverse=True)

print sorting_emp
