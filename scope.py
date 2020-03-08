#legb rule
#c=0

'''def test():
    c=2
    print c

test()
print c'''

x='global x'

def outer():
    x='outer x'
    
    def inner():
        x='inner x'
        print x
    inner() #inner x
    print x #outer x
outer()
print x






