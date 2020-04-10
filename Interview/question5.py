# How do you find the largest and smallest number in an unsorted integer array?
array = [9,29,39,1,2,5,6,100] 

'''
    Pro: Find what you need
    Con: Have to sort the array.
    Time: O(n)
'''
def find_max_and_min_num_print(array):
    array.sort()
    max_num = array[-1]
    min_num = array[0]
    for i in range(0, len(array)):
        if array[i] == max_num:
            print("Max Number: %d"%max_num) 
        elif (array[i] == min_num):
            print("Min Number: %d"%min_num)

find_max_and_min_num_print(array)

'''
    Pro: Find what you need
    Time: O(n)
'''
def find_max_and_min_num(array):
    max_num = array[-1]
    min_num = array[0]
    for num in array:
        if max_num < num:
            max_num = num
        elif (min_num > num):
            min_num = num

    return min_num, max_num
print(find_max_and_min_num(array))