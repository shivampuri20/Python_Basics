import csv
import os 
print  "%s"%os.getcwd()
#dirs= os.listdir('\Users\user\Desktop\pythonfiles')
#print dirs

#with open('csvnames.csv','r') as csv_file: #reading a csv file
    #csv_read=csv.reader(csv_file)
    
    #with open('newnames.csv','w') as new_file:
       # csv_write=csv.writer(new_file,delimiter='-')  #writing a csv file
       # for line in csv_read:
            #print(line[2])
            #csv_write.writerow(line)

#WORKING WITH DICT READERS

with open('csvnames.csv','r') as csv_file: #reading a csv file
    csv_read=csv.DictReader(csv_file)

   #for line in csv_read:
       # print(line['email'])
    with open('newnames.csv','w') as new_file:
         fieldnames= ['first_name','lsatname','email']  # to create for new directory
         csv_write=csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='-')  #writing a csv file
         csv_write.writeheader()
         for line in csv_read:
             del line['email']
            # print(line[2])
             #csv_write.writerow(line)
