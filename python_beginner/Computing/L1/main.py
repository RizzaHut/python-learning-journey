def calculate_damage(sword, arrow, spear, dagger, fireball):
    weapons = [sword, arrow, spear, dagger, fireball]
    total_damage = sum(weapons)
    average_damage = sum(weapons) / len(weapons)
    return total_damage, average_damage
