import math 
def log_scale(data: list[float], base: float) -> list[float]:
    log_data = []

    for d in data:
        log_data.append(math.log(d, base))

    return log_data
