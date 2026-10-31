def area_sum(rectangles: list[dict[str, int]]) -> int:
    area: int = 0
    for r in rectangles:
        area += r["height"] * r["width"]
    return area
            
