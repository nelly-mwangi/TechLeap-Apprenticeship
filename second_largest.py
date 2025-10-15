def second_largest(nums):
    if len(nums) < 2:
        return None
    unique_nums = sorted(set(nums), reverse=True)
    return unique_nums[1] if len(unique_nums) > 1 else None


