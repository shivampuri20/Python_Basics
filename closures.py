def outer_func(msg):
    message=msg

    def inner_func():
        print(message)

    return inner_func #without executing the function we are returning 

hi_func=outer_func('hi')
hello_func=outer_func('hello')

#print myfunc.__name__

print hi_func() 
print hello_func()  #with the help of closures we can easily extend the scope to invoke a inner function outside its scope































