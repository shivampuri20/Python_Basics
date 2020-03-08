#property decorators
import logging 
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#or
formatter=logging.Formatter('%(levelname)s:%(name)s%(message)s')
file_handler=logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



#logging.basicConfig(filename='employee.log', level=logging.INFO,format='%(levelname)s:%(name)s%(message)s')

class Employee:
    no_of_emp=0
    raise_amt=1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last
        
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property   # it is added because we do not want to access email as method but as attribute.
    def email(self):
        return '{}{}@gmail.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
       print 'delete name'
       self.first=None
       self.last =None

emp_1 = Employee('Corey', 'Schafer' )
emp_2 = Employee('Test', 'Employee')

#emp_1.first='jim'
emp_1.fullname='corey scharafer'

print emp_1.first
print emp_1.email
print emp_1.fullname


del emp_1.fullname
