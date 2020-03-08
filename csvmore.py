import csv

html_output=''
names=[]

with open ('info.csv','r') as data_file:
    csv_data=csv.reader(data_file)
    next(csv_data) #for next line in csv file
    next(csv_data)

   # print list(csv_data)
    for line in csv_data:
        if line[0] =='No Reward':
            break
        names.append('{} {}'.format(line[0],line[1]))   #alternate we can use fstring

#for name in names:
    #print name


html_output += '<p> there are curently {} public contributors</p>'.format(len(names))
for name in names:
    html_output += '\n\t<li>{}</li>'.format(name)

html_output +='\n</ul>'
print html_output























