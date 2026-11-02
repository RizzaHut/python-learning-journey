import pytest
from main import Archer, Crossbowman

run_cases = [
    ("Will", 1, "Darren", 4, None, 1),
    ("Elena", 5, "Connor", 3, None, 0),
]

submit_cases = [
    pytest.param("Jake", 0, "Victor", 3, None, 0, marks=pytest.mark.submit),
    pytest.param(
        "Ryan", 2, "Emma", 1, "not enough arrows", None, marks=pytest.mark.submit
    ),
    pytest.param("Zoe", 10, "Lucas", 8, None, 5, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    (
        "archer_name",
        "archer_arrows",
        "crossbowman_name",
        "crossbowman_bolts",
        "expected_exception",
        "expected_remaining_bolts",
    ),
    run_cases + submit_cases,
)
def test_triple_shot(
    archer_name,
    archer_arrows,
    crossbowman_name,
    crossbowman_bolts,
    expected_exception,
    expected_remaining_bolts,
):
    print("\n---------------------------------")
    print(f"Archer: {archer_name}, Arrows: {archer_arrows}")
    archer = Archer(archer_name, archer_arrows)
    print(f"Crossbowman: {crossbowman_name}, Arrows: {crossbowman_bolts}")
    print()
    crossbowman = Crossbowman(crossbowman_name, crossbowman_bolts)
    try:
        expected_str = f"{archer_name} was shot by 3 crossbow bolts"
        actual_str = crossbowman.triple_shot(archer)
        actual_exception = None
    except Exception as error:
        actual_str = None
        actual_exception = str(error)

    if expected_exception is not None or actual_exception is not None:
        print(f"Expected exception: {expected_exception}")
        print(f"Actual exception:   {actual_exception}")
        assert actual_exception == expected_exception
        return

    print(f"Expected triple_shot message: {expected_str}")
    print(f"Actual triple_shot message:   {actual_str}")
    print(f"Expected remaining bolts: {expected_remaining_bolts}")
    print(f"Actual remaining bolts:   {crossbowman.get_num_arrows()}")
    assert actual_exception is None
    assert actual_str == expected_str
    assert crossbowman.get_num_arrows() == expected_remaining_bolts
