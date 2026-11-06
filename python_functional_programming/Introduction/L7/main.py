def format_line(line: str) -> str:
    strip_space = line.rstrip()
    capitalize = strip_space.upper()
    remove_period = capitalize.replace(".", "")
    return f"{remove_period}...."
