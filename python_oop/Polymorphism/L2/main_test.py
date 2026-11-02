import pytest
from main import Rectangle

run_cases = [
    ((1, 2, 3, 4), (1, 3, 4, 2)),
    ((3, 4, 1, 2), (1, 3, 4, 2)),
]

submit_cases = [
    pytest.param((5, 4, 2, 1), (2, 5, 4, 1), marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("rect_args", "expected_output"), run_cases + submit_cases)
def test_getters(rect_args, expected_output):
    rectangle = Rectangle(rect_args[0], rect_args[1], rect_args[2], rect_args[3])
    print("\n---------------------------------")
    print("Inputs Rectangle:")
    print(f" * x1: {rect_args[0]}")
    print(f" * y1: {rect_args[1]}")
    print(f" * x2: {rect_args[2]}")
    print(f" * y2: {rect_args[3]}")
    print()

    expected_left_x, expected_right_x, expected_top_y, expected_bottom_y = (
        expected_output
    )

    actual_left_x = rectangle.get_left_x()
    actual_right_x = rectangle.get_right_x()
    actual_top_y = rectangle.get_top_y()
    actual_bottom_y = rectangle.get_bottom_y()

    print(f"Expected left x: {expected_left_x}")
    print(f"Actual   left x: {actual_left_x}")
    print(f"Expected right x: {expected_right_x}")
    print(f"Actual   right x: {actual_right_x}")
    print(f"Expected top y: {expected_top_y}")
    print(f"Actual   top y: {actual_top_y}")
    print(f"Expected bottom y: {expected_bottom_y}")
    print(f"Actual   bottom y: {actual_bottom_y}")

    result = (actual_left_x, actual_right_x, actual_top_y, actual_bottom_y)
    assert result == expected_output
