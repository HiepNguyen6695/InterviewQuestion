# How do you find ANY duplicate number on a given integer array?

array = [1,2,3,4,5,6,3,4]

def find_multidup_num(arr):
    n = len(arr)
    count = [0] * n # Set every item in the count list to be 0

    for i in range(0, n):
        if count[arr[i]] == 1:
            print(arr[i])
        else:
            count[arr[i]] = count[arr[i]] + 1
    print(count)

find_multidup_num(array)