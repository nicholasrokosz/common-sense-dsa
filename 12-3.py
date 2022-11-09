# same as 11-5.py, but using memoization

def unique_paths(rows, columns, memo={}):
    print('ran')
    if rows == 1 or columns == 1:
        return 1

    if str([rows, columns]) not in memo and str([columns, rows]) not in memo:
        memo[str([rows, columns])] = memo[str([columns, rows])] = unique_paths(rows-1, columns, memo) + unique_paths(rows, columns-1, memo)

    return memo[str([rows, columns])]




print(unique_paths(4, 3))
