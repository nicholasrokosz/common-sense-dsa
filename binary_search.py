def binary_search(arr, n):
    hi = len(arr) - 1
    lo = 0

    while lo <= hi:
        mid = (hi + lo) // 2

        if arr[mid] < n:
            lo = mid + 1
        elif arr[mid] > n:
            hi = mid - 1
        else:
            return mid

    return -1


print(binary_search([1, 3, 6, 12, 20, 33, 34, 45, 55, 72, 99], 33))
