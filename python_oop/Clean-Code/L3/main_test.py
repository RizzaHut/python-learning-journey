import ast
import inspect
import textwrap

import pytest
from main import fight_soldiers, get_soldier_dps

run_cases = [
    (
        {"damage": 10, "attacks_per_second": 3},
        {"damage": 20, "attacks_per_second": 1},
        "soldier 1 wins",
    ),
    (
        {"damage": 50, "attacks_per_second": 1},
        {"damage": 50, "attacks_per_second": 2},
        "soldier 2 wins",
    ),
]

submit_cases = [
    pytest.param(
        {"damage": 1, "attacks_per_second": 1},
        {"damage": 2, "attacks_per_second": 1},
        "soldier 2 wins",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        {"damage": 100, "attacks_per_second": 2},
        {"damage": 50, "attacks_per_second": 4},
        "both soldiers die",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("soldier_one", "soldier_two", "expected"), run_cases + submit_cases
)
def test_fight_soldiers(soldier_one, soldier_two, expected):
    print("\n---------------------------------")
    source = textwrap.dedent(inspect.getsource(fight_soldiers))
    tree = ast.parse(source)
    calls_helper = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "get_soldier_dps"
        for node in ast.walk(tree)
    )
    if not calls_helper:
        print("Please call get_soldier_dps inside fight_soldiers!")
    assert calls_helper
    print("Soldier one:")
    print(f"  damage: {soldier_one['damage']}")
    print(f"  attacks_per_second: {soldier_one['attacks_per_second']}")
    print("Soldier two:")
    print(f"  damage: {soldier_two['damage']}")
    print(f"  attacks_per_second: {soldier_two['attacks_per_second']}")
    print(f"Expected: {expected}")
    result = fight_soldiers(soldier_one, soldier_two)
    print(f"Actual:   {result}")
    assert result == expected

    actual_soldier_one_dps = get_soldier_dps(soldier_one)
    actual_soldier_two_dps = get_soldier_dps(soldier_two)
    expected_soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
    expected_soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
    if actual_soldier_one_dps != expected_soldier_one_dps:
        print(f"Expected soldier one dps: {expected_soldier_one_dps}")
        print(f"Actual soldier one dps:   {actual_soldier_one_dps}")
    assert actual_soldier_one_dps == expected_soldier_one_dps
    if actual_soldier_two_dps != expected_soldier_two_dps:
        print(f"Expected soldier two dps: {expected_soldier_two_dps}")
        print(f"Actual soldier two dps:   {actual_soldier_two_dps}")
    assert actual_soldier_two_dps == expected_soldier_two_dps
