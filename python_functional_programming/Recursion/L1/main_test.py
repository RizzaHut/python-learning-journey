import pytest
from main import factorial_r

run_cases = [
    (3, 6),
    (5, 120),
    (0, 1),
]

submit_cases = [
    pytest.param(1, 1, marks=pytest.mark.submit),
    pytest.param(2, 2, marks=pytest.mark.submit),
    pytest.param(10, 3628800, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("n", "expected"), run_cases + submit_cases)
def test_factorial_r(n: int, expected: int) -> None:
    print("\n---------------------------------")
    print(f"Input: {n}")
    print(f"Expected: {expected}")
    result = factorial_r(n)
    print(f"Actual:   {result}")
    assert result == expected
