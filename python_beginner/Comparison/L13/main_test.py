import pytest
from main import combat_evaluation

run_cases = [
    (101, 100, True, False, False),
    (50, 100, False, True, False),
    (100, 100, False, False, True),
]

submit_cases = [
    pytest.param(150, 70, True, False, False, marks=pytest.mark.submit),
    pytest.param(80, 150, False, True, False, marks=pytest.mark.submit),
    pytest.param(0, 0, False, False, True, marks=pytest.mark.submit),
    pytest.param(1, 1, False, False, True, marks=pytest.mark.submit),
    pytest.param(1000, 500, True, False, False, marks=pytest.mark.submit),
    pytest.param(500, 1000, False, True, False, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "expected_output1", "expected_output2", "expected_output3"),
    run_cases + submit_cases,
)
def test_combat_evaluation(
    input1, input2, expected_output1, expected_output2, expected_output3
):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    result = combat_evaluation(input1, input2)
    print(f"Expected: {expected_output1}, {expected_output2}, {expected_output3}")
    print(f"Actual:   {result}")
    assert result == (expected_output1, expected_output2, expected_output3)
