import pytest
from main import Dragon

run_cases = [
    (("Smaug", "red"), "I am Smaug, the red dragon"),
    (("Saphira", "blue"), "I am Saphira, the blue dragon"),
]

submit_cases = [
    pytest.param(
        ("Eldrazi", "colorless"),
        "I am Eldrazi, the colorless dragon",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ("Glaurung", "gold"),
        "I am Glaurung, the gold dragon",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ("Fafnir", "green"),
        "I am Fafnir, the green dragon",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("args", "expected_output"), run_cases + submit_cases)
def test_str(args, expected_output):
    print("\n---------------------------------")
    print(f"Name: {args[0]}, Color: {args[1]}")
    print()
    print(f"Expected: {expected_output}")
    dragon = Dragon(*args)
    result = str(dragon)
    print(f"Actual:   {result}")
    assert result == expected_output
