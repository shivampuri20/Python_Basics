import random

#value=random.random()  b/w 0 and 1
#print value 

#print dir(random)

#value=random.uniform(1,10)  # b/w floating value of 1 and 10
#print value

#value=random.randint(1,10)  # b/w integer value of 1 and 10
#print value


greetings=['hello','hi','hey','hola']
colors =['red','black','green']

#value=random.choice(greetings)
#print value +'corey'

#results=random.choices(colors,k=10) 
#print results

#results=random.choice(colors,weights=[18,18,4],k=10) #weights are used to tell probability of occurence of colors
#print results

deck =list(range(1,53))
random.shuffle(deck)
hand=random.sample(deck,k=5)
print hand
