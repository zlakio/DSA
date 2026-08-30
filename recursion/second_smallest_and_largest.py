def second_largest(head):
    largest = head[0]
    for i in range(0, len(head)):
        if head[i] > largest:
            largest = head[i]

    slargest = float("-inf")
    for i in range(0, len(head)):
        if head[i] > slargest and head[i] != largest:
            slargest = head[i]

    if slargest == float("-inf"):
        return None
    return slargest


def second_smallest(head):
    smallest = head[0]
    for i in range(0, len(head)):
        if head[i] < smallest:
            smallest = head[i]

    ssmallest = float("inf")
    for i in range(0, len(head)):
        if head[i] != smallest and head[i] < ssmallest:
            ssmallest = head[i]

    if ssmallest == float("inf"):
        return None
    return ssmallest


head = [5, 5, 5]
print(second_largest(head), second_smallest(head))
