import pytest
from main import convert_case

run_cases = [
    pytest.param(
        "Through the darkness of future past",
        "uppercase",
        "THROUGH THE DARKNESS OF FUTURE PAST",
    ),
    pytest.param("The magician longs to see", "lowercase", "the magician longs to see"),
]

submit_cases = [
    pytest.param(
        "One chants out between two worlds",
        "titlecase",
        "One Chants Out Between Two Worlds",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "Fire walk with me",
        "garbagecase",
        "unsupported format: garbagecase",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("text", "target_case", "expected"), run_cases + submit_cases)
def test_convert_case(text, target_case, expected):
    print("\n---------------------------------")
    print("Input:")
    print(f'"{text}", {target_case}')
    print("Expected:")
    print(f'"{expected}"')
    try:
        result = convert_case(text, target_case)
    except Exception as error:
        result = str(error)
    print("Actual:")
    print(f'"{result}"')
    assert result == expected
