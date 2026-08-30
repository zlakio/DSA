def print_one_to_n(i, n):
    i: int
    n: int
    if i < 1:
        return
    print_one_to_n(i - 1, n)
    print(i)


print_one_to_n(8, 8)
