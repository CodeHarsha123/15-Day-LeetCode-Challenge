def two_sum(nums, target):
    prev_map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return []  # In case no solution is found

# Example usage:
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))  # Output: [0, 1]