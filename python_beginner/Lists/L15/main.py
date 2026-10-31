def get_champion_slices(champions):
    third_to_end = champions[2:]
    all_except_last = champions[:len(champions)-1]
    even = champions[::2]
    return third_to_end, all_except_last, even
