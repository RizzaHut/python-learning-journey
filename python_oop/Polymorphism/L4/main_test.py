import pytest
from main import Dragon

run_cases = [
    (Dragon("Green Dragon", -1, -2, 1, 2, 1), -2, -3, 0, 0, True),
    (Dragon("Red Dragon", 2, 2, 2, 2, 2), 0, 1, 1, 0, True),
    (Dragon("Gold Dragon", 0, 0, 5, 5, 10), 4, 0, 5, 1, False),
    (Dragon("Blue Dragon", 4, -3, 2, 1, 1), 0, 0, 10, 10, False),
]

submit_cases = [
    pytest.param(
        Dragon("Orange Dragon", 0, 0, 20, 20, 20),
        10,
        10,
        20,
        20,
        True,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Dragon("Black Dragon", 5, -1, 3, 2, 2),
        -10,
        -10,
        10,
        10,
        True,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Dragon("Tall Dragon", 0, 0, 10, 2, 1),
        0,
        4,
        1,
        5,
        True,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("dragon", "x1", "y1", "x2", "y2", "expected_output"),
    run_cases + submit_cases,
)
def test_in_area(dragon, x1, y1, x2, y2, expected_output):
    print("\n---------------------------------")
    print(f" * Dragon pos_x: {dragon.pos_x}")
    print(f" * Dragon pos_y: {dragon.pos_y}")
    print(f" * Dragon height: {dragon.height}")
    print(f" * Dragon width: {dragon.width}")
    print()
    print(f" * Area x1: {x1}")
    print(f" * Area y1: {y1}")
    print(f" * Area x2: {x2}")
    print(f" * Area y2: {y2}")
    print()
    result = dragon.in_area(x1, y1, x2, y2)
    print(f"Expected in area: {expected_output}")
    print(f"Actual in area:   {result}")
    assert result == expected_output
