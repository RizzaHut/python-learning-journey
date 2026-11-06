import pytest
from main import get_median_font_size

run_cases = [
    pytest.param([4, 3, 2, 1, 5], 3),
    pytest.param([20, 14, 16], 16),
    pytest.param([9, 11, 16, 20], 11),
    pytest.param([], None),
]

submit_cases = [
    pytest.param([8, 8, 8], 8, marks=pytest.mark.submit),
    pytest.param([30, 18, 14, 22], 18, marks=pytest.mark.submit),
    pytest.param([6, 24, 6, 6, 24, 24, 2, 1, 3], 6, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("input_sizes", "expected"), run_cases + submit_cases)
def test_get_median_font_size(input_sizes, expected):
    print("\n---------------------------------")
    print(f"Input: {input_sizes}")
    print(f"Expected: {expected}")
    input_copy = input_sizes.copy()
    result = get_median_font_size(input_sizes)
    print(f"Actual: {result}")
    assert result == expected
    if input_sizes != input_copy:
        print(f"Expected font_sizes: {input_copy}")
        print(f"Actual font_sizes: {input_sizes}")
        print("font_sizes was modified")
    assert input_sizes == input_copy
