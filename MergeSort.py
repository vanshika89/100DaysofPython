import random


def merge_sort(array):
    if len(array) <= 1: # Base case: arrays of length 1 or less are already sorted
        return

    # Spliting the array into two halves
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]

    # Recursively sorting the two halves
    merge_sort(left_array)
    merge_sort(right_array)

    # Merging the sorted arrays into the original array
    i = j = k = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    # Copy any remaining elements
    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1


input_array = [random.randint(1, 100) for _ in range(10)]
print("Random input array:", input_array)
merge_sort(input_array)
print("Sorted array", input_array)
