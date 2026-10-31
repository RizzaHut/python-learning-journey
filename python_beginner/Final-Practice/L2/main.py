def find_min(nums: list[int]) -> int | float:
    min_so_far: float = float("inf")
    min_num: int = 0
    if not nums:
        return float("inf")
    for num in nums:
        if num < min_so_far:
            min_so_far = num
    return min_so_far
