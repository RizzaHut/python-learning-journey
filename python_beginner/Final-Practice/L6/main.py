def divide_list(nums: list[int], divisor: int) -> list[float]:
    divided: list[float] = []
    for num in nums:
        divided.append(float(num / divisor))
    return divided

