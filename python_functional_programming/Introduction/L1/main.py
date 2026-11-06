def stylize_title(document: str) -> str:
    centered_doc = center_title(document)
    return add_border(centered_doc)


# Don't touch below this line


def center_title(document: str) -> str:
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document: str) -> str:
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)
