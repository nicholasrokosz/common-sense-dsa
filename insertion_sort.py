def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        pos = i - 1

        while pos >= 0:
            if arr[pos] > tmp:
                arr[pos + 1] = arr[pos]
                pos -= 1
            else:
                break

        arr[pos + 1] = tmp

    return arr


print(insertion_sort([1, 99, 6, 5, 50, 42, 9, 2]))
