def square(x):
    return x*x

#f=square

#print square
#print f(5) #functions as objects


#def my_map(func,arg_list):
#    result =[]
#    for i in arg_list:
 #       result.append(func(i))
  #  return result
#squares =my_map(square,[1,2,3,4,5]) #using another function in these function as an argument 

#print squares

def logger(msg):
    def logmessage():   #using one function into another function
        print 'log:',msg

    return logmessage

log_hi=logger('hiii')
log_hi()




























