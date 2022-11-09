def add_until_100(arr):
    if len(arr) == 0:
        return 0
    
    subproblem_result = add_until_100(arr[1:])

    if arr[0] + subproblem_result > 100:
        return subproblem_result
    else:
        return arr[0] + subproblem_result


print(add_until_100([40, 50, 11]))
