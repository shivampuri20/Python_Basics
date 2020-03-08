def decorator_func(original_func):

    def wrapper_func(*args,**kwargs):
        print'wrapper executed before {}'.format(original_func.__name__)
        return original_func(*args,**kwargs)

    return wrapper_func

#class decorator_class(object):   #class decorator
    #def __init__(self,original_func):
        #self.original_func=original_func

    #def __call__(self,*args,**kwargs):
     #   print'call method  executed before {}'.format(self.original_func.__name__)
      #  return self.original_func(*args,**kwargs)

@decorator_func
def display():
    print 'display func ran'

#decorator_display=decorator_func(display)              
#decorator_display() 

#note:
#decorator_display=decorator_func(display) this is equal to @decorator_func
#decorator_display()


@decorator_func
def display_info(name,age):
    print 'display_info ran with arguments ({} , {})'.format(name,age)

display_info('john',25)

display()
