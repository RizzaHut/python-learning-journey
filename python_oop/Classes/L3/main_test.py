import pytest
from main import Wall

run_cases = [(Wall(), [50, 100, 200])]

submit_cases = [
    pytest.param(
        Wall(),
        [50, 100, 200, 400, 800, 1600, 3200],
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("wall", "expected_outputs"), run_cases + submit_cases)
def test_get_cost(wall, expected_outputs):
    print("\n---------------------------------")
    actual_outputs = []
    for _ in expected_outputs:
        cost = wall.get_cost()
        actual_outputs.append(cost)
        print(f"Wall cost: {cost}")
        wall.fortify()
        print("fortifying wall...")
    print(f"Expected: {expected_outputs}")
    print(f"Actual:   {actual_outputs}")
    assert actual_outputs == expected_outputs
