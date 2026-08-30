def check(nums):
    largest = nums[0]
    boolean = True
    for i, num in enumerate(nums):
        if num >= largest:
            boolean = True
            largest = num
        else:
            boolean = False

    return boolean


nums = [1, 2, 3, 8]

print(check(nums))
