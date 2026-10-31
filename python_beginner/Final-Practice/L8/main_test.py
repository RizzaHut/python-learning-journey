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

    if not luck_boosts:
        assert expected_avg == 0.0
        with pytest.raises(ZeroDivisionError) as error:
            avg_luck_boost(luck_boosts)
        print(f"Caught ZeroDivisionError: {error.value}")
        return

    avg = avg_luck_boost(luck_boosts)
    print(f"Expected average boost: {expected_avg}")
    print(f"Actual average boost:   {avg}")
    assert isclose(avg, expected_avg)


@pytest.mark.submit
def test_run_cases():
    assert len(run_cases) == 5
    assert sum(not case["luck_boosts"] for case in run_cases) == 1
