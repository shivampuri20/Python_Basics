import os
from datetime import datetime 
print  "%s"%os.getcwd()  #get current directory

os.chdir('\Users\user\Desktop')
print  "%s"%os.getcwd()
 
#os.makedirs('os-demo') #make a directory 

print os.stat('r.txt').st_size
dirs= os.listdir('\Users\user\Desktop')
print dirs


#for dirpath,dirnames,filenames in os.walk('\Users\user\Desktop'):
#   print "current path: ",dirpath
#   print "dir name is ",dirnames
#   print "filename is :",filenames
#   print ".."


print "%s"%os.environ.get('HOME')

print os.path.exists('\Users\user\Desktop\run.py')
