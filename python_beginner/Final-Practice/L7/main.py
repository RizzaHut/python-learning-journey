def join_strings(strings: list[str]) -> str:
    if not strings:
        return ""
    sentence: str = strings[0]
    for string in strings[1:]:
        sentence += "," + string
    return sentence

