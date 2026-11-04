def average_followers(nums: list[int]) -> float | None:
    if not nums:
        return None
    return sum(nums) / len(nums)