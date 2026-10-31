def remove_nonints(nums: list[object]) -> list[int]:
    int_list: list[int] = []
    for num in nums:
        if type(num) == int:
            int_list.append(num)
    return int_list
