import pytest
from main import sum_of_numbers

run_cases = [(0, 5, 10), (0, 10, 45), (10, 20, 145)]

submit_cases = [
    pytest.param(1, 100, 4950, marks=pytest.mark.submit),
    pytest.param(5, 50, 1215, marks=pytest.mark.submit),
    pytest.param(20, 30, 245, marks=pytest.mark.submit),
    pytest.param(50, 60, 545, marks=pytest.mark.submit),
    pytest.param(100, 110, 1045, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "expected_output"), run_cases + submit_cases
)
def test_sum_of_numbers(input1, input2, expected_output):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * start: {input1}")
    print(f" * end: {input2}")
    result = sum_of_numbers(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
