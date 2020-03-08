test ="test string"

def find_index(search,target):
    for i,value in enumerate(search):
        if value == target:
            return i
    return -1 
