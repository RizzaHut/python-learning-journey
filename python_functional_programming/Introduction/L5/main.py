def get_median_font_size(font_sizes: list[int]) -> int | None:
    sorted_list = sorted(font_sizes)
    mid_num = len(sorted_list) // 2
    if mid_num % 2 == 0:
        return (sorted_list[mid_num - 1] + sorted_list[mid_num]) // 2
    return sorted_list[mid_num]
