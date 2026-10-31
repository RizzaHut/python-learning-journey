from math import isclose

import pytest
from main import avg_luck_boost
from test_cases import run_cases


@pytest.mark.parametrize("case", run_cases)
def test_avg_luck_boost(case):
    print("\n---------------------------------")
    luck_boosts = case["luck_boosts"]
    expected_avg = case["expected_avg"]
    print(f"Party luck boosts: {luck_boosts}")

    assert isinstance(luck_boosts, list)
    assert isinstance(expected_avg, float)

    avg = avg_luck_boost(luck_boosts)
    print(f"Expected average boost: {expected_avg}")
    print(f"Actual average boost:   {avg}")
    assert isclose(avg, expected_avg)
