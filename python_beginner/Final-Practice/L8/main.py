def avg_luck_boost(luck_boosts: list[int]) -> float:
    total = 0
    for boost in luck_boosts:
        total += boost
    return total / len(luck_boosts)
