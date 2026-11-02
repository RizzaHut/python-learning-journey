import pytest
from main import Rectangle, Square

run_cases = [
    ((2, 4), 8, 12),
    ((5,), 25, 20),
]

submit_cases = [
    pytest.param((1, 1), 1, 4, marks=pytest.mark.submit),
    pytest.param((3, 4), 12, 14, marks=pytest.mark.submit),
    pytest.param((6, 7), 42, 26, marks=pytest.mark.submit),
    pytest.param((8,), 64, 32, marks=pytest.mark.submit),
    pytest.param((9, 10), 90, 38, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("inputs", "expected_area", "expected_perimeter"), run_cases + submit_cases
)
def test_shape(inputs, expected_area, expected_perimeter):
    print("\n---------------------------------")
    if len(inputs) == 2:
        shape = Rectangle(*inputs)
        shape_type = "Rectangle"
    else:
        shape = Square(inputs[0])
        shape_type = "Square"

    print(f"Testing {shape_type} with inputs {inputs}")
    area = shape.get_area()
    perimeter = shape.get_perimeter()
    print(f"Expected area: {expected_area}")
    print(f"Actual area:   {area}")
    print(f"Expected perimeter: {expected_perimeter}")
    print(f"Actual perimeter:   {perimeter}")
    assert (area, perimeter) == (expected_area, expected_perimeter)
