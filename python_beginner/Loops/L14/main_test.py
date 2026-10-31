import pytest
from main import calculate_experience_points

run_cases = [
    (2, 5),
    (3, 15),
    (4, 30),
]

submit_cases = [
    pytest.param(1, 0, marks=pytest.mark.submit),
    pytest.param(5, 50, marks=pytest.mark.submit),
    pytest.param(7, 105, marks=pytest.mark.submit),
    pytest.param(10, 225, marks=pytest.mark.submit),
    pytest.param(15, 525, marks=pytest.mark.submit),
    pytest.param(20, 950, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_calculate_experience_points(input1, expected_output):
    print("\n---------------------------------")
    result = calculate_experience_points(input1)
    print(f"Input:     {input1}")
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
