def shift_zeroes(next):
    j = -1
    n = len(next)
    for i in range(0, n):
        if next[i] == 0:
            j = i
            break
    else:
        return next
    for i in range(j + 1, n):
        if next[i] != 0:
            next[i], next[j] = next[j], next[i]
            j += 1

    return next


print(shift_zeroes(next=[1, 2, 3, 1]))
