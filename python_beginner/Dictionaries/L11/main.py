def merge(dict1, dict2):
    merged_guild = {}

    for k in dict1:
        merged_guild[k] = dict1[k]

    for k in dict2:
        merged_guild[k] = dict2[k]

    return merged_guild
