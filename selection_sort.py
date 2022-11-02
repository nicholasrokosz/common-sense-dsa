def selection_sort(arr):
    for i in range(len(arr) - 1):
        lowest_number_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_number_index]:
                lowest_number_index = j

        if lowest_number_index != i:
            arr[i], arr[lowest_number_index] = arr[lowest_number_index], arr[i]

    return arr



print(selection_sort([45, 68, 2, 4, 1, 99, 86, 3]))
