def valid(num):
    b = str(num)
    n = len(b)
    j = -1
    for i in range(0, n // 2):
        if b[i] != b[j]:
            return False
        j = j - 1
    return True


print(valid(1232))
