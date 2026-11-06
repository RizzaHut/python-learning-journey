import pytest
from main import format_line

run_cases = [
    pytest.param(
        "You can't spell America without Erica",
        "YOU CAN'T SPELL AMERICA WITHOUT ERICA...",
    ),
    pytest.param("Friends don't lie.", "FRIENDS DON'T LIE..."),
    pytest.param(
        " She's our friend and she's crazy!",
        "SHE'S OUR FRIEND AND SHE'S CRAZY!...",
    ),
]

submit_cases = [
    pytest.param(
        " You're gonna slay 'em dead, Nance. ",
        "YOU'RE GONNA SLAY 'EM DEAD, NANCE...",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input_line", "expected"), run_cases + submit_cases)
def test_format_line(input_line, expected):
    print("\n---------------------------------")
    print(f"Input: {input_line}")
    print(f"Expected: {expected}")
    result = format_line(input_line)
    print(f"Actual: {result}")
    assert result == expected
