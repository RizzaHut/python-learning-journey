def count_nested_levels(
    nested_documents: dict[int, dict], target_document_id: int, level: int = 1
) -> int:
    # base case
    if not nested_documents:
        return -1

    # make data smaller
    for doc_id, sub_nested_doc in nested_documents.items():
        if doc_id == target_document_id:
            return level
        if isinstance(sub_nested_doc, dict):
            
            # recursive step
            recursion_result = count_nested_levels(sub_nested_doc, target_document_id, level + 1)
            if recursion_result != -1:
                return recursion_result
    return -1
    

