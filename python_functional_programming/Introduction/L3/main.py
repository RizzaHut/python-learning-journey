def add_prefix(document: str, documents: tuple[str, ...]) -> tuple[str, ...]:
    prefix = f"{len(documents)}. "
    new_doc: tuple[str, ...] = (prefix + document, )
    upd_documents: tuple[str, ...] = documents + new_doc
    return upd_documents
