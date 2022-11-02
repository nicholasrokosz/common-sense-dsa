def bubble_sort(arr):
    sorted_past_index = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True

        for i in range(sorted_past_index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

        sorted_past_index -= 1

    return arr




print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))
