# How is an integer array sorted in place using the quicksort algorithm?
# arr[j] is not sorted
# low = 0
# high = n - 1
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quicksort(arr, low, high):
    if low < high:
        n = partition(arr, low, high)

        quicksort(arr, low, n - 1)
        quicksort(arr, n + 1, high)


array = [4,3,2,4,6,7,3,2,3]
n = len(array)
quicksort(array, 0, n - 1)

for i in range(0, n):
    print(array[i])


            