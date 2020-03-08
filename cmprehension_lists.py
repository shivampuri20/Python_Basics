nums =[1,2,3,4,5,6,7,8,9,10]

#my_list =[]
#for n in nums:
#    my_list.append(n)
#print my_list

#my_list=[n*n for n in nums] #comprehension  
#print my_list

#my_list=[n for n in nums if n%2==0]  #to find even nums
#print my_List

#my_list=map(lambda n: n*n ,nums) #map function
#print my_list


#my_list=[]
#for letter in 'abcd':
 #   for num in range(0,4):
  #      my_list.append((letter,num))
#print my_list


#my_list=[letter,num for letter in 'abcd' for num in range(4)]
#print my_list

names=['peter','logan','bruce']
heroes=['spiderman','batman','hulk']

#my_dict={}
#for name,hero in zip(names,heroes):
 #   my_dict[name]=hero
#print my_dict

my_dict={name : hero for name , hero in zip(names,heroes)}  #dict comprehension using zip function
print my_dict


num=[1,2,3,4,5,6,7,8,9,9,5,4]
#my_set=set()
#for n in num:
 #   my_set.add(num)
#print my_set

my_set ={n for n in num} #set comprehension
print my_set

#generator expression
my_gen=(n*n for n in nums)
for i in my_gen:
    print i 




