def find_minimum(nums: list[int]) -> float | None:
    smallest_so_far = float("inf")

    if not nums:
        return None
    for num in nums:
        if num < smallest_so_far:
            smallest_so_far = num
    return smallest_so_far