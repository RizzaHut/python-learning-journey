def get_follower_prediction(
    follower_count: int, influencer_type: str, num_months: int
) -> int:
    total = 0
    if influencer_type == "fitness":
        total = follower_count * (4 ** num_months)
        return total
    elif influencer_type == "cosmetic":
        total = follower_count * (3 ** num_months)
        return total
    total = follower_count * (2 ** num_months)
    return total
