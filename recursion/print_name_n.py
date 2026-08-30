def printname(name, count, n):

    name: str
    n: int
    count: int
    if count > n:
        return
    print(name)
    printname(name, count + 1, n)


printname("jessica", 1, 10)
