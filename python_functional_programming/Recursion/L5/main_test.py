import pytest
from main import sum_nested_list

NestedList = list[int | list]

run_cases = [
    ([1, 2, [3, 4]], 10),
    ([5, [6, 7], [[8, 9], 10]], 45),
]

submit_cases = [
    pytest.param([], 0, marks=pytest.mark.submit),
    pytest.param(
        [1, [2], [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]],
        55,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input_list", "expected"), run_cases + submit_cases)
def test_sum_nested_list(input_list: NestedList, expected: int) -> None:
    print("\n---------------------------------")
    print(f"Input list: {input_list}")
    print(f"Expected output: {expected}")
    result = sum_nested_list(input_list)
    print(f"Actual output: {result}")
    assert result == expected
