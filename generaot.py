def sq_no(nums):
    #result =[]
    for i in nums:
        yield(i*i)
my_nums=sq_no([1,2,3,4,5])

#print next(my_nums)

print list(my_nums)
