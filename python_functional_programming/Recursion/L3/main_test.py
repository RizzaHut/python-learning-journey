import pytest
from main import zipmap

MovieRatings = dict[str, float]

run_cases = [
    (
        ["The Grand Budapest Hotel", "Fantastic Mr. Fox", "Moonrise Kingdom"],
        [8.1, 7.9, 7.8],
        {
            "The Grand Budapest Hotel": 8.1,
            "Fantastic Mr. Fox": 7.9,
            "Moonrise Kingdom": 7.8,
        },
    ),
    (
        ["The Royal Tenenbaums", "The Life Aquatic with Steve Zissou", "Isle of Dogs"],
        [7.6, 7.3, 7.9],
        {
            "The Royal Tenenbaums": 7.6,
            "The Life Aquatic with Steve Zissou": 7.3,
            "Isle of Dogs": 7.9,
        },
    ),
]

submit_cases = [
    pytest.param([], [], {}, marks=pytest.mark.submit),
    pytest.param([""], [], {}, marks=pytest.mark.submit),
    pytest.param([], [0.0], {}, marks=pytest.mark.submit),
    pytest.param(
        [
            "Rushmore",
            "The Darjeeling Limited",
            "The French Dispatch",
            "The Wonderful Story of Henry Sugar and Three More",
        ],
        [7.7, 7.2, 7.4],
        {
            "Rushmore": 7.7,
            "The Darjeeling Limited": 7.2,
            "The French Dispatch": 7.4,
        },
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ["Bottle Rocket", "Asteroid City", "The Grand Budapest Hotel"],
        [7.0, 7.6, 8.1, 0.0],
        {
            "Bottle Rocket": 7.0,
            "Asteroid City": 7.6,
            "The Grand Budapest Hotel": 8.1,
        },
        marks=pytest.mark.submit,
    ),
]


def print_dict(d: MovieRatings) -> None:
    for key, value in sorted(d.items()):
        print(f" * {key}: {value}")


@pytest.mark.parametrize(("keys", "values", "expected"), run_cases + submit_cases)
def test_zipmap(keys: list[str], values: list[float], expected: MovieRatings) -> None:
    print("\n---------------------------------")
    print(f"Inputs: {keys}, {values}")
    print("Expected:")
    print_dict(expected)
    result = zipmap(keys, values)
    print("Actual:")
    print_dict(result)
    assert result == expected
