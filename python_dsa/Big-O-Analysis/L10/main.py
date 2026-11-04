def count_names(list_of_lists: list[list[str]], target_name: str) -> int:
    name_counter = 0

    for list in list_of_lists:
        for name in list:
            if name == target_name:
                name_counter += 1

    return name_counter
