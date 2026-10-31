import pytest
from main import check_mount_rental

run_cases = [
    (3, 4, "no charges yet"),
    (5, 2, "overtime charged"),
]

submit_cases = [
    pytest.param(2, 2, "overtime charged", marks=pytest.mark.submit),
    pytest.param(0, 1, "no charges yet", marks=pytest.mark.submit),
    pytest.param(1, 1, "overtime charged", marks=pytest.mark.submit),
    pytest.param(100, 2, "overtime charged", marks=pytest.mark.submit),
    pytest.param(2500, 3, "overtime charged", marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "expected_output"), run_cases + submit_cases
)
def test_check_mount_rental(input1, input2, expected_output):
    print("\n---------------------------------")
    print(f"Inputs: {input1}, {input2}")
    result = check_mount_rental(input1, input2)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
