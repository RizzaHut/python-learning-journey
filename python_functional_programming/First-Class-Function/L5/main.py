def remove_invalid_lines(document: str) -> str:
    doc_list = document.split("\n")
    filtered_doc = list(filter(lambda doc: not doc.startswith("-"), doc_list ))
    return "\n".join(filtered_doc)
