def restore_documents(originals: tuple[str, ...], backups: tuple[str, ...]) -> set[str]:
    combined_doc = set(map(str.upper, originals + backups))
    print(combined_doc)  
    filtered_doc = set(filter(lambda doc: not doc[2].isdigit(), combined_doc))
    return filtered_doc