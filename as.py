class Animal(object):
    pass
## this reprsent a is-a relation 
class Dog(Animal):
    def __init__(self,name):
        ##has-a
        self.name=name
    def sound(self,sound):
        self.sound=sound
        print "sound of ",self.name,"=" ,self.sound
       
## is-a
class Cat(Animal):
    def __init__(self ,name):
        ##has-a
        self.name=name
## is-a
class Person(object):
    def __init__(self ,name):
        ##has-a
        self.name=name
        self.pet=None
## has-a
class Emp(Person):
    def __init__(self,name,salary):
        super(Emp,self).__init__(name)
        ##g=has-a
        self.salary=salary

class Fish(object):
    pass
class Salmon(Fish):
    pass
rover=Dog("rover")
satan=Cat("satan")
mary=Person("mary")
mary.pet=satan
frank=Emp("Frank",20000)
frank.pet=rover
print frank.name

thomas=Dog("thomas")
thomas.sound("bau")





	






