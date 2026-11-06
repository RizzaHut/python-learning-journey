valid_formats: list[str] = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(
    doc_names: list[str], doc_formats: list[str]
) -> list[tuple[str, str]]:
    doc_tuples = list(zip(doc_names, doc_formats))
    filtered_doc = list(filter(lambda doc: doc[1] in valid_formats, doc_tuples))
    return filtered_doc
