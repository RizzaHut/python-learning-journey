def find_last_name(names_dict: dict[str, str], first_name: str) -> str | None:
    if first_name in names_dict:
        return names_dict[first_name]
