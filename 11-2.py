def evens_only(arr, evens=[]):
    if not arr:
        return evens

    return evens_only(arr[1:], [*evens, arr[0]] if arr[0] % 2 == 0 else evens)






print(evens_only([1, 2, 3, 4, 5, 6, 7, 8, 9]))
