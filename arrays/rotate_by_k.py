def rotate_left(next, k):
    temp = []
    n = len(next)
    for i in range(0, k):
        temp.append(next[i])
    for i in range(k, n):
        next[i - k] = next[i]
    for i in range(n - k, n):
        next[i] = temp[i - (n - k)]
    return next


print(rotate_left(next=[1, 2, 3, 4, 5], k=2))
