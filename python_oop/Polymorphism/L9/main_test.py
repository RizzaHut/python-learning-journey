import pytest
from main import Card

run_cases = [
    ("Ace", "Hearts", "Queen", "Hearts", False, True),
    ("2", "Spades", "2", "Hearts", False, True),
]

submit_cases = [
    pytest.param(
        "Ace", "Spades", "Ace", "Spades", True, False, marks=pytest.mark.submit
    ),
    pytest.param("3", "Diamonds", "7", "Clubs", False, False, marks=pytest.mark.submit),
    pytest.param(
        "King", "Clubs", "King", "Hearts", False, False, marks=pytest.mark.submit
    ),
    pytest.param(
        "Queen", "Diamonds", "Jack", "Spades", False, True, marks=pytest.mark.submit
    ),
    pytest.param("10", "Hearts", "10", "Hearts", True, False, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("rank_1", "suit_1", "rank_2", "suit_2", "expected_eq", "expected_gt"),
    run_cases + submit_cases,
)
def test_card_comparison(rank_1, suit_1, rank_2, suit_2, expected_eq, expected_gt):
    print("\n---------------------------------")
    print(f"Inputs: {rank_1} of {suit_1}, {rank_2} of {suit_2}")
    print("Expected:")
    print(f" * Equal: {expected_eq}")
    print(f" * Greater than: {expected_gt}")
    print(f" * Less than: {not (expected_eq or expected_gt)}")

    card_1 = Card(rank_1, suit_1)
    card_2 = Card(rank_2, suit_2)
    result_eq = card_1 == card_2
    result_gt = card_1 > card_2
    result_lt = card_1 < card_2
    print("Actual:")
    print(f" * Equal: {result_eq}")
    print(f" * Greater than: {result_gt}")
    print(f" * Less than: {result_lt}")
    assert result_eq == expected_eq
    assert result_gt == expected_gt
    assert result_lt == (not (expected_eq or expected_gt))
