import pytest
from main import Card, HighCardRound, LowCardRound

run_cases = [
    (Card("Ace", "Spades"), Card("2", "Clubs"), 1, 2),
    (Card("Queen", "Hearts"), Card("Queen", "Diamonds"), 1, 2),
]

submit_cases = [
    pytest.param(
        Card("10", "Clubs"), Card("10", "Spades"), 2, 1, marks=pytest.mark.submit
    ),
    pytest.param(
        Card("King", "Hearts"),
        Card("Queen", "Spades"),
        1,
        2,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Card("2", "Diamonds"),
        Card("2", "Diamonds"),
        0,
        0,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Card("5", "Clubs"), Card("10", "Hearts"), 2, 1, marks=pytest.mark.submit
    ),
    pytest.param(
        Card("Jack", "Spades"),
        Card("2", "Spades"),
        1,
        2,
        marks=pytest.mark.submit,
    ),
]


def result_to_card(card1, card2, placement):
    if placement == 1:
        return card1
    if placement == 2:
        return card2
    return "Tie"


@pytest.mark.parametrize(
    ("card1", "card2", "expected_high_winner", "expected_low_winner"),
    run_cases + submit_cases,
)
def test_rounds(card1, card2, expected_high_winner, expected_low_winner):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * card1: {card1}")
    print(f" * card2: {card2}")

    print("\nTesting HighCardRound:")
    high_round = HighCardRound(card1, card2)
    high_result = high_round.resolve_round()
    expected_winner = result_to_card(card1, card2, expected_high_winner)
    actual_winner = result_to_card(card1, card2, high_result)
    print(f"Expected winner: {expected_winner}")
    print(f"Actual winner:   {actual_winner}")

    print("\nTesting LowCardRound:")
    low_round = LowCardRound(card1, card2)
    low_result = low_round.resolve_round()
    expected_winner = result_to_card(card1, card2, expected_low_winner)
    actual_winner = result_to_card(card1, card2, low_result)
    print(f"Expected winner: {expected_winner}")
    print(f"Actual winner:   {actual_winner}")

    assert high_result == expected_high_winner
    assert low_result == expected_low_winner
