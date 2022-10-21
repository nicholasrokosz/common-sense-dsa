def greatestNumber(arr):
    greatest = arr[0]

    for n in arr[1:]:
        if n > greatest:
            greatest = n
    return greatest

print(greatestNumber([1, 2, 3, 4, 1, 8, 4, 9]))
