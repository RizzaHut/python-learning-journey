import pytest
from main import check_swords_for_army

run_cases = [
    (500, 1000, "incorrect amount"),
    (800, 800, "correct amount"),
]

submit_cases = [
    pytest.param(1500, 1000, "incorrect amount", marks=pytest.mark.submit),
    pytest.param(200, 200, "correct amount", marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "expected_output"), run_cases + submit_cases
)
def test_check_swords_for_army(input1, input2, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    result = check_swords_for_army(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
