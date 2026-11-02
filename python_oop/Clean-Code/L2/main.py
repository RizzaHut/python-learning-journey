def calculate_remaining_health(health: int, damage: int) -> int:
    return health - damage


print(calculate_remaining_health(100, 25))
