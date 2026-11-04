def does_name_exist(
    first_names: list[str], last_names: list[str], full_name: str
) -> bool:
    for f in first_names:
        for l in last_names:
            name = f + " " + l
            if name == full_name:
                return True
    return False
