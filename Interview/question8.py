# How are duplicates removed from a given array in Java?
array = [1,2,3,4,5,3]

def remove_dup_with_lib(arr):
    newSet = set()
    for num in arr:
        if not newSet.__contains__(num):
            newSet.add(num)
    print("Original Array")
    print(arr)
    print("Duplicates Removed")
    print(list(newSet))

remove_dup_with_lib(array)