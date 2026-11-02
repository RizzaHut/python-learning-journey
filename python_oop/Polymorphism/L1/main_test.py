import pytest
from main import Rectangle

run_cases = [
    ((0, 1, 4, 2), 0, 1, 4, 2),
    ((5, 5, 0, 0), 5, 5, 0, 0),
]

submit_cases = [
    pytest.param((-10, -10, -5, -5), -10, -10, -5, -5, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input_args", "expected_x1", "expected_y1", "expected_x2", "expected_y2"),
    run_cases + submit_cases,
)
def test_rectangle(input_args, expected_x1, expected_y1, expected_x2, expected_y2):
    print("\n---------------------------------")
    print(f"Input arguments: {input_args}")
    print()

    rectangle = Rectangle(*input_args)

    print(f"Expected x1: {expected_x1}")
    print(f"Actual   x1: {rectangle.x1}")
    print(f"Expected y1: {expected_y1}")
    print(f"Actual   y1: {rectangle.y1}")
    print(f"Expected x2: {expected_x2}")
    print(f"Actual   x2: {rectangle.x2}")
    print(f"Expected y2: {expected_y2}")
    print(f"Actual   y2: {rectangle.y2}")

    assert (rectangle.x1, rectangle.y1, rectangle.x2, rectangle.y2) == (
        expected_x1,
        expected_y1,
        expected_x2,
        expected_y2,
    )
