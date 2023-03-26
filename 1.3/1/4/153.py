def array_front9(nums):
    for i in range(min(len(nums), 4)):
        if nums[i] == 9:
            return True
    return False


print(array_front9([1, 2, 3, 4, 5, 6]))