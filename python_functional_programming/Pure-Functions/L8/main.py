def word_count_memo(document: str, memos: dict[str, int]) -> tuple[int, dict[str, int]]:
    pass


# Don't edit below this line


def word_count(document: str) -> int:
    count = len(document.split())
    return count
