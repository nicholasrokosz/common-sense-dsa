def nth_triangular_num(n):
    if n == 1:
        return 1

    return n + nth_triangular_num(n - 1)


print(nth_triangular_num(8))
