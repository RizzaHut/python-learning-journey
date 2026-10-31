def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name not in enemies_dict:
            enemies_dict[enemy_name] = 0
        enemies_dict[enemy_name] += 1
    return enemies_dict
