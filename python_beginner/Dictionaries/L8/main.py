def get_most_common_enemy(enemies_dict):
    max_enemy = float("-inf")
    enemy_name = ""

    if not enemies_dict:
        return None

    for name in enemies_dict:
        if enemies_dict[name] > max_enemy:
            max_enemy = enemies_dict[name]
            enemy_name = name
    return enemy_name

