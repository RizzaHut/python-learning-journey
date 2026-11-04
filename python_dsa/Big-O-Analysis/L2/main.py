def find_max(nums: list[float]) -> float:
    biggest_so_far = float("-inf")

    for num in nums:
        if num > biggest_so_far:
            biggest_so_far = num
    return biggest_so_far
