person ={'name':'renny','age':'23'}

#sentence = 'my name is {0} and i am {1} years old .'.format(person['name'],person['age'])   #fstring
#print sentence

l=['renny',23]
sentence ='my name is {0[0]} and my age is {0[1]}'.format(l)

sentence ='my name is {name} and my age is {age} '.format(**person)
print sentence

for i in range(1,10):
    sentence = 'value is {:03}'.format(i)
    print sentence

 
import datetime
my_date= datetime.datetime(2016,9,24,12,30,45)

sentence="{0:%B %d ,%Y}fell on a {0:%A} and was the {0:%j}day of the year".format(my_date)  #0 is added because we have three placeholders and we are only adding one value in format so we write 0 to have comman single index value 
print sentence




