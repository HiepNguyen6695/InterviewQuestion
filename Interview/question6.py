# How do you find all pairs of an integer array whose sum is equal to a given number?

'''
    Pro: Get what you want
    Time: O(n)
'''
given_sum = 6
array = [0,1,2,3,4,6,7,5]

def find_all_pairs(arr, given_sum):
    if len(arr) < 2:
        return arr

    Set = set()

    for num in arr:
        target = given_sum - num
        if not Set.__contains__(target):
            Set.add(num)
        else:
            print(num, target)


find_all_pairs(array, given_sum)

'''
    Pro: Get what you want
    Time: O(n)
'''
def find_all_pairs_wit_left_right(arr, given_sum):
    n = len(arr)
    left = 0
    right = n - 1
    arr.sort()

    while left < right:
        # Calculate the sum
        sum_target = arr[left] + arr[right]

        if sum_target == given_sum:
            print(arr[left], arr[right])
            left += 1
            right -= 1
        elif sum_target < given_sum:
            left += 1
        elif sum_target > given_sum:
            right -= 1
        

find_all_pairs_wit_left_right(array, given_sum)