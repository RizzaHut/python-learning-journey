import pytest
from main import Archer

run_cases = [
    (
        Archer("Robin", 6, 2),
        Archer("Sheriff", 3, 4),
        1,
        [(5, 1), (2, 3)],
        None,
    ),
    (
        Archer("Friar Tuck", 1, 0),
        Archer("Prince John", 1, 0),
        1,
        [None, None],
        "Friar Tuck can't shoot",
    ),
]

submit_cases = [
    pytest.param(
        Archer("Guy of Gisborne", 0, 1),
        Archer("Sheriff", 3, 2),
        1,
        [None, None],
        "Guy of Gisborne is dead",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Archer("Little John", 4, 4),
        Archer("Sheriff", 3, 2),
        4,
        [None, None],
        "Sheriff is dead",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("archer_1", "archer_2", "rounds", "expected_result", "expected_err"),
    run_cases + submit_cases,
)
def test_archer_duel(archer_1, archer_2, rounds, expected_result, expected_err):
    print("\n---------------------------------")
    print("Initial Status:")
    archer_1.print_status()
    archer_2.print_status()

    error = None
    archer_1_health = None
    archer_1_arrows = None
    archer_2_health = None
    archer_2_arrows = None
    try:
        for round_num in range(1, rounds + 1):
            print(f"\nRound {round_num}:")
            print(f"* {archer_1.name}'s turn:")
            archer_1.shoot(archer_2)
            archer_2.print_status()
            print(f"* {archer_2.name}'s turn:")
            archer_2.shoot(archer_1)
            archer_1.print_status()

        print("\nFinal Status:")
        archer_1.print_status()
        archer_2.print_status()
        if expected_err:
            print(
                f"\nTest Failed: Expected error '{expected_err}' but no exception was raised"
            )
        else:
            _, archer_1_health, archer_1_arrows = archer_1.get_status()
            _, archer_2_health, archer_2_arrows = archer_2.get_status()
    except Exception as caught_error:
        error = caught_error

    if error is not None:
        error_msg = str(error)
        print()
        print(f"Expected exception: {expected_err}")
        print(f"Actual exception:   {error_msg}")
        assert expected_err is not None
        assert error_msg == expected_err
        return

    assert expected_err is None

    archer_1_expected = expected_result[0]
    archer_2_expected = expected_result[1]
    if archer_1_expected is None or archer_2_expected is None:
        print("\nTest Failed: expected results are missing")
    assert archer_1_expected is not None and archer_2_expected is not None

    archer_1_expected_health, archer_1_expected_arrows = archer_1_expected
    archer_2_expected_health, archer_2_expected_arrows = archer_2_expected
    print("\nResults Check:")
    print(f"Expected {archer_1.name} health: {archer_1_expected_health}")
    print(f"Actual {archer_1.name} health:   {archer_1_health}")
    print(f"Expected {archer_1.name} arrows: {archer_1_expected_arrows}")
    print(f"Actual {archer_1.name} arrows:   {archer_1_arrows}")
    print(f"Expected {archer_2.name} health: {archer_2_expected_health}")
    print(f"Actual {archer_2.name} health:   {archer_2_health}")
    print(f"Expected {archer_2.name} arrows: {archer_2_expected_arrows}")
    print(f"Actual {archer_2.name} arrows:   {archer_2_arrows}")
    assert (
        archer_1_health == archer_1_expected_health
        and archer_1_arrows == archer_1_expected_arrows
        and archer_2_health == archer_2_expected_health
        and archer_2_arrows == archer_2_expected_arrows
    )
