import sys

list=[ 'a',0,2]

for entry in list:
    try:
        print "entry is ",entry 
        r = 1/int(entry)
        break

    except:
        print"oops", sys.exc_info()[0],"occured"
        print "next entry is "
print "reciprocal is " ,r
