import pytest
from main import Wall

run_cases = [
    (10, 5, 20),
    (20, 5, 40),
]

submit_cases = [
    pytest.param(320, 5, 640, marks=pytest.mark.submit),
    pytest.param(640, 5, 1280, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("armor", "height", "expected"), run_cases + submit_cases)
def test_fortify(armor, height, expected):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * armor:  {armor}")
    print(f" * height: {height}")
    print(f"Expected: {expected}")
    wall = Wall()
    wall.armor = armor
    wall.height = height
    wall.fortify()
    result = wall.armor
    print(f"Actual:   {result}")
    assert result == expected
