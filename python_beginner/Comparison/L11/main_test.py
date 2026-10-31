import pytest
from main import should_serve_customer

run_cases = [
    (22, False, 10, True),
    (41, False, 1, False),
    (14, False, 7, False),
]

submit_cases = [
    pytest.param(21, False, 5, True, marks=pytest.mark.submit),
    pytest.param(107, False, 9, True, marks=pytest.mark.submit),
    pytest.param(23, True, 5, False, marks=pytest.mark.submit),
    pytest.param(21, False, 4, False, marks=pytest.mark.submit),
    pytest.param(57, False, 11, False, marks=pytest.mark.submit),
    pytest.param(20, False, 5, False, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "input3", "expected_output"), run_cases + submit_cases
)
def test_should_serve_customer(input1, input2, input3, expected_output):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * customer_age: {input1}")
    print(f" * on_break: {input2}")
    print(f" * time: {input3}")
    result = should_serve_customer(input1, input2, input3)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    assert result == expected_output
