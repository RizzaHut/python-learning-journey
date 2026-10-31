import pytest
from main import meditate

run_cases = [
    (0, 10, 9, [9, 0]),
    (0, 12, 20, [12, 8]),
    (0, 10, 0, [0, 0]),
    (1, 100, 80, [81, 0]),
]

submit_cases = [
    pytest.param(0, 0, 0, [0, 0], marks=pytest.mark.submit),
    pytest.param(1000, 1000, 5, [1000, 5], marks=pytest.mark.submit),
    pytest.param(0, 10, 5, [5, 0], marks=pytest.mark.submit),
    pytest.param(5, 2000, 500, [505, 0], marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input1", "input2", "input3", "expected"), run_cases + submit_cases
)
def test_meditate(input1, input2, input3, expected):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" *           mana: {input1}")
    print(f" *       max_mana: {input2}")
    print(f" *    num_potions: {input3}")
    result = meditate(input1, input2, input3)
    result_mana = None
    result_potions = None
    if result is not None:
        result_mana, result_potions = result
    print(f"Expected: mana {expected[0]}, potions {expected[1]}")
    print(f"Actual:   mana {result_mana}, potions {result_potions}")
    assert result_mana == expected[0] and result_potions == expected[1]
