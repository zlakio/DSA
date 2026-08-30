def f(i, n, l):
    if i >= n * 0.5:
        return

    l[i], l[n - i - 1] = l[n - i - 1], l[i]

    f(i + 1, n, l)


l = [1, 2, 3, 4]
f(0, len(l), l)

print(l)
