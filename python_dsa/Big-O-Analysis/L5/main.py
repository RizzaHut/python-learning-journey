def get_avg_brand_followers(all_handles: list[list[str]], brand_name: str) -> float:
    brand_count = 0
    total_account = 0
    for handle in all_handles:
        for follower in handle:
            if brand_name in follower:
                brand_count += 1
    return brand_count / len(all_handles)
