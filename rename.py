import os 

os.chdir('E:\Hollywood movies')

print "%s"%os.getcwd()

for f in os.listdir('E:\Hollywood movies'):
    filename,file_ext= os.path.splitext(f)
  # print file_ext
   #print filename.split('-')
    ftitle ,flabel =filename.split('-')
   #print ftitle
    newname= '{}-{}-{}'.format(ftitle,file_ext,flabel)
    os.rename(f,newname)

