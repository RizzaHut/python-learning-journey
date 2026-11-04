import math


def get_influencer_score(
    num_followers: int, average_engagement_percentage: float
) -> float:
    influencer_score = average_engagement_percentage * (math.log(num_followers, 2))
    return float(influencer_score)
