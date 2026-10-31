import pytest
from main import sum_of_odd_numbers

run_cases = [
    (4, 4),
    (6, 9),
]

submit_cases = [
    pytest.param(0, 0, marks=pytest.mark.submit),
    pytest.param(1, 0, marks=pytest.mark.submit),
    pytest.param(2, 1, marks=pytest.mark.submit),
    pytest.param(4, 4, marks=pytest.mark.submit),
    pytest.param(10, 25, marks=pytest.mark.submit),
    pytest.param(15, 49, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("input1", "expected_output"), run_cases + submit_cases)
def test_sum_of_odd_numbers(input1, expected_output):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * end: {input1}")
    result = sum_of_odd_numbers(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
