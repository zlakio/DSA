def sum_of_numbers(i, sum):
    if i < 1:
        print(sum)  # executes when i is 0 otherwise it wont print shit
        return
    sum_of_numbers(i - 1, sum + i)


sum_of_numbers(5, 0)
