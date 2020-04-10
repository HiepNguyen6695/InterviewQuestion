# How do you find ANY duplicate number on a given integer array?
'''
    Pro: Get what you need
    Con: Get 2 dup next to each other (Have to sort array)
    Time Complexity: O(n)
    Space: O(n)
'''
array = [1,1,2,2,3,5,4,4,5]

def find_one_dup_num(array):
    n = len(array) # n = 6
    count = [0] * n
    for i in range(0, n):
        if (count[array[i]] == 1):
            print(array[i])
        else:
            count[array[i]] = count[array[i]] + 1
        
find_one_dup_num(array)