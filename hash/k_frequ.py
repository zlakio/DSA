def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    s = {}
    for i in nums:
        if i in s:
            s[i] += 1
        else:
            s[i] = 1

    sort_items = sorted(s.items(), key=lambda x: x[1], reverse=True)
    result = []
    for i in range(k):
        result.append(sort_items[i][0])

    return result
