def file(*args,**kwargs):
    print(args)
    print(kwargs)
student=['smith','john','rohan']
course={'course1':'arts','course2':'compsci'}
    

file(*student,**course)
