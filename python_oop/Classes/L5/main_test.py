import pytest
from main import Wall

run_cases = [
    (Wall(2, 3, 4), (2, 3, 4, 24)),
    (Wall(4, 5, 6), (4, 5, 6, 120)),
]

submit_cases = [
    pytest.param(Wall(22, 23, 24), (22, 23, 24, 12144), marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("wall", "expected_output"), run_cases + submit_cases)
def test_constructor(wall, expected_output):
    print("\n---------------------------------")
    expected_depth, expected_height, expected_width, expected_volume = expected_output
    print("Expected wall:")
    print("  - volume:", expected_volume)
    print("  - depth: ", expected_depth)
    print("  - height:", expected_height)
    print("  - width: ", expected_width)
    print("Actual wall:")
    print("  - volume:", wall.volume)
    print("  - depth: ", wall.depth)
    print("  - height:", wall.height)
    print("  - width: ", wall.width)
    assert (
        expected_volume == wall.volume
        and expected_depth == wall.depth
        and expected_height == wall.height
        and expected_width == wall.width
    )
