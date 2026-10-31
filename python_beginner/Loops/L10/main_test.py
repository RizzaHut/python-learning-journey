import pytest
from main import regenerate

run_cases = [(0, 10, 20, 9), (0, 10, 4, 1), (8, 10, 20, 10)]

submit_cases = [
    pytest.param(0, 0, 0, 0, marks=pytest.mark.submit),
    pytest.param(9, 10, 3, 9, marks=pytest.mark.submit),
    pytest.param(100, 100, 200, 100, marks=pytest.mark.submit),
    pytest.param(2, 110, 50, 26, marks=pytest.mark.submit),
    pytest.param(100, 1010, 2000, 1010, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "input3", "expected_output"), run_cases + submit_cases
)
def test_regenerate(input1, input2, input3, expected_output):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * current_health: {input1}")
    print(f" *     max_health: {input2}")
    print(f" * enemy_distance: {input3}")
    print(f"Expected Health: {expected_output}")
    result = regenerate(input1, input2, input3)
    print(f"  Actual Health: {result}")
    assert result == expected_output
