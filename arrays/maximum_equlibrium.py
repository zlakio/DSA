def pivotIndex(nums):
    n = len(nums)
    s = sum(nums)
    left = 0
    right = 0
    for i in range(n):
        right = s - left - nums[i]

        if right == left:
            return i
        left = left + nums[i]
    return -1


print(pivotIndex(nums=[2, 0, 2, 3, 4]))
