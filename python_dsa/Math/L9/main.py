def decayed_followers(
    initial_followers: int, fraction_lost_daily: float, days: int
) -> float:
    retention_rate = 1.0 - fraction_lost_daily
    remaining_followers = initial_followers * (retention_rate ** days)
    return float(remaining_followers)

