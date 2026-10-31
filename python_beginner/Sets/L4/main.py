def find_missing_ids(first_ids, second_ids):
    first_ids_set = set(first_ids)
    second__ids_set = set(second_ids)

    unique_ids = first_ids_set - second__ids_set

    return unique_ids
