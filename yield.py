
def square():
    i=1
    while True:
        yield i*i
        i=i+1   #return do not execute from here 
 
for num in square():
      if num>100:
          break
      print num   

