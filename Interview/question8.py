# How are duplicates removed from a given array in Java?
array = [12,3,44,8,4,3,4]
array.sort()
n = len(array)
def remove_dup(arr, n):
    
    if n == 0 or n == 1: 
        return n 
    count = 0
    for i in range(0, n - 1):
        if arr[i] != arr[i+1]:
            arr[count] = arr[i]
            count += 1
            #print(count)
            #print(arr)
        else:
            print(arr[i])
    arr[count] = arr[n - 1]
    count += 1
    return count

remove_dup(array, n)

#for i in range(0, n):
#    print(array[i])
