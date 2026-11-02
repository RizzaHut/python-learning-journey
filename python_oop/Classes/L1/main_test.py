import pytest
from main import BatteringRam, Wall

run_cases = [(Wall, {"armor": 10, "height": 5})]

submit_cases = [
    pytest.param(
        BatteringRam,
        {"damage": 2, "length": 4},
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("class_type", "expected_attributes"), run_cases + submit_cases
)
def test_class_attributes(class_type, expected_attributes):
    print("\n---------------------------------")
    print(f"Testing class: {class_type.__name__}")
    instance = class_type()
    passed = True

    for attr_name, expected_value in expected_attributes.items():
        if hasattr(instance, attr_name):
            actual_value = getattr(instance, attr_name)
            print(f"Expected {attr_name}: {expected_value}")
            print(f"Actual {attr_name}:   {actual_value}")
            if actual_value != expected_value:
                passed = False
        else:
            print(f"Error: {attr_name} attribute not found")
            passed = False

    assert passed
