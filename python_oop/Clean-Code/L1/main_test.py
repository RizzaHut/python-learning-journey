import pytest
from main import destroy_walls

run_cases = [
    ([0, 20, 30], [20, 30]),
    ([10, 0, 40, 0], [10, 40]),
]

submit_cases = [
    pytest.param([], [], marks=pytest.mark.submit),
    pytest.param([3, 2, 0, 3, 0, 0], [3, 2, 3], marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("wall_healths", "expected"), run_cases + submit_cases)
def test_destroy_walls(wall_healths, expected):
    print("\n---------------------------------")
    print(f"Input:     {wall_healths}")
    print(f"Expected: {expected}")
    result = destroy_walls(wall_healths)
    print(f"Actual:   {result}")
    assert str(result) == str(expected)
