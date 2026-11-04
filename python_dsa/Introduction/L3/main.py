def summed(nums: list[int]) -> int:
    total = 0
    if not nums:
        return total
    for num in nums:
        total += num
    return total
