from typing import Any

import pytest
from main import hex_to_rgb

run_cases = [
    pytest.param("00FFFF", (0, 255, 255), None),
    pytest.param("FFFF00", (255, 255, 0), None),
    pytest.param("Hello!", None, "not a hex color string"),
    pytest.param("42", None, "not a hex color string"),
    pytest.param(1_000_000, None, "not a hex color string"),
]

submit_cases = [
    pytest.param("", None, "not a hex color string", marks=pytest.mark.submit),
    pytest.param("FF00FF00", None, "not a hex color string", marks=pytest.mark.submit),
    pytest.param("FF00FF", (255, 0, 255), None, marks=pytest.mark.submit),
    pytest.param("000000", (0, 0, 0), None, marks=pytest.mark.submit),
    pytest.param("FFFFFF", (255, 255, 255), None, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("input_hex", "expected", "expected_error"), run_cases + submit_cases
)
def test_hex_to_rgb(input_hex: Any, expected, expected_error):
    print("\n---------------------------------")
    print(f"  Inputs: '{input_hex}'")
    try:
        result = hex_to_rgb(input_hex)
    except Exception as error:
        print(f"Expected Error: {expected_error}")
        print(f"  Actual Error: {error}")
        assert str(error) == expected_error
        return
    if expected_error is not None:
        print(f"Expected Error: {expected_error}")
        print(f"        Actual: {result} (no error thrown)")
    assert expected_error is None
    print(f"Expected: {expected}")
    print(f"  Actual: {result}")
    assert result == expected
