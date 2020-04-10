# How do you find THE missing number in a given integer array of 1 to 100?

'''
    Pro: Return one missing number.
    Con: Doesn't have ability to get multiple missing number
'''
array = [1,2,4,5,6,7,8,9,10,11,12,13,14,15]

def missing_number(array):
    i, n, total = 0,len(array), 1

    for i in range(2, n + 2):
        total += i # total in the array
        #print ('%d:%d' % (i, total))
        total -= array[i - 2] 
    return total

print('Missing number: %d '%(missing_number(array)))

def find_missing_num(arr):
    n = len(arr)
    total = (n) * (n + 1) // 2
    temp = 0
    for i in range(0, n - 1):
        temp += arr[i]

    total -= temp
    print(total)

find_missing_num(array)