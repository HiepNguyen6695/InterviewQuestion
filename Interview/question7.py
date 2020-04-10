# How do you find duplicate numbers in an array if it contains multiple duplicates?

'''
    Time Complexity: O(n)
    Space: O(1)
'''

array = [4,3,2,4,6,8,6,1,9,8,8,8]

def find_dup_num(array):
    n = len(array)
    # Calculate each num in the ray
    for i in range(n):
        array[array[i] % n] = array[array[i] % n] + n

def print_result(array):
    find_dup_num(array)
    n = len(array)
    for j in range(n):
        if (array[j] > n*2):
            print(j)

print_result(array)