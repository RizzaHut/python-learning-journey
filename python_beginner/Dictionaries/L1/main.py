def get_character_record(name, server, level, rank):
    user = {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}"
    }
    return user
