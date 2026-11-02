import pytest
from main import Rectangle

run_cases = [
    (Rectangle(0, 0, 4, 4), Rectangle(3, 3, 6, 6), True),
    (Rectangle(0, 0, 4, 4), Rectangle(5, 5, 8, 8), False),
]

submit_cases = [
    pytest.param(
        Rectangle(0, 0, 1, 1),
        Rectangle(4, 4, 5, 5),
        False,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Rectangle(1, 1, 4, 4),
        Rectangle(2, 2, 3, 3),
        True,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Rectangle(1, 1, 2, 2),
        Rectangle(0, 0, 4, 4),
        True,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Rectangle(1, 1, 4, 4),
        Rectangle(1, 1, 4, 4),
        True,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Rectangle(0, 0, 4, 1),
        Rectangle(1, 2, 3, 3),
        False,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Rectangle(0, 0, 4, 4),
        Rectangle(5, 0, 8, 4),
        False,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Rectangle(10, 0, 14, 4),
        Rectangle(0, 0, 4, 4),
        False,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Rectangle(0, 0, 2, 2),
        Rectangle(2, 0, 4, 2),
        True,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Rectangle(0, 0, 2, 2),
        Rectangle(2, 2, 4, 4),
        True,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("rect1", "rect2", "expected_overlap"), run_cases + submit_cases
)
def test_overlap(rect1, rect2, expected_overlap):
    print("\n---------------------------------")
    print("Checking overlap of:")
    print(f" - {rect1}")
    print(f" - {rect2}")
    print()
    print(f"Expected overlap: {expected_overlap}")

    result = rect1.overlaps(rect2)
    print(f"Actual overlap:   {result}")
    assert result == expected_overlap
