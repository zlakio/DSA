def twoSum(self, nums, target):
    s = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in s:
            return [s[comp], i]
        s[num] = i
