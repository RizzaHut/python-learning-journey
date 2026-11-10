def sum_nested_list(lst: list[int | list]) -> int:
    total_so_far = 0
    
    for i in lst:
        if isinstance(i, int):
            total_so_far += i
        elif isinstance(i, list):
            total_so_far += sum_nested_list(i)
    return int(total_so_far) 