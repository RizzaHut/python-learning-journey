def get_estimated_spread(audiences_followers: list[int]) -> float:
    if not audiences_followers:
        return 0.0
    num_followers = len(audiences_followers)
    average_followers = sum(audiences_followers) / num_followers
    estimated_spread = float(average_followers * ( num_followers ** 1.2 ) )
    return estimated_spread