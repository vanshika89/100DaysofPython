import random


def merge_sort(array):
    if len(array) <= 1:  # already sorted
        return

    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]

    # calling merge sort on each array
    merge_sort(left_array)
    merge_sort(right_array)

    # merging the sorted arrays
    i = j = k = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1


input_array = [random.randint(1, 100) for _ in range(0, 10)]
print('Input array :', input_array)
sorted_array = merge_sort(input_array)
print('Sorted array', input_array)
