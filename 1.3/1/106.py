def max_end3(nums):
    max_element = max(nums[0], nums[-1])

    return [max_element] * 3


print(max_end3([1, 2, 3]))