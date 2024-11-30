def mergeSort(array):
    if len(array) <= 1:
        return

    # Split the array into two halves
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]

    # Recursively sort the two halves
    mergeSort(left_array)
    mergeSort(right_array)

    # Merge the sorted halves back into the original array
    i = 0
    j = 0
    k = 0
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


input_array = [2, 6, 2, 8, 9, 6, 7, 3]
mergeSort(input_array)
print("Sorted array:", input_array)
