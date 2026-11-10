def zipmap(keys: list[str], values: list[float]) -> dict[str, float]:
    if not keys or not values:
        return {}
    current_pair = {keys[0]: values[0]}
    new_pair = zipmap(keys[1:], values[1:])
    return {**current_pair, **new_pair}