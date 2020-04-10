# How do you remove duplicates from an array in place? 
array = [1,2,3,4,5,6,3] 

def remove_dup_in_place(arr):
    res = [] 
    [res.append(x) for x in arr if x not in res] 
    print(str(res))
remove_dup_in_place(array)