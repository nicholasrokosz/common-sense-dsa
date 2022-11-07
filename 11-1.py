def number_of_chars(arr):
    if len(arr) == 1:
        return len(arr[0])

    return len(arr[0]) + number_of_chars(arr[1:])




print(number_of_chars(['ab', 'c', 'def', 'ghij']))
