import pytest
from main import Sword

run_cases = [
    (Sword("bronze"), Sword("bronze"), "iron", None),
    (Sword("bronze"), Sword("iron"), None, "cannot craft"),
]

submit_cases = [
    pytest.param(
        Sword("steel"),
        Sword("steel"),
        None,
        "cannot craft",
        marks=pytest.mark.submit,
    ),
    pytest.param(Sword("iron"), Sword("iron"), "steel", None, marks=pytest.mark.submit),
    pytest.param(
        Sword("bronze"),
        Sword("steel"),
        None,
        "cannot craft",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("sword1", "sword2", "expected_result", "expected_err"),
    run_cases + submit_cases,
)
def test_craft(sword1, sword2, expected_result, expected_err):
    print("\n---------------------------------")
    print(f"{sword1.sword_type} sword + {sword2.sword_type} sword...")
    try:
        result = sword1 + sword2
        actual_err = None
    except Exception as error:
        result = None
        actual_err = str(error)

    if expected_err is not None or actual_err is not None:
        print(f"Expected Exception: {expected_err}")
        print(f"Actual Exception:   {actual_err}")
        assert actual_err == expected_err
        return

    assert result is not None
    print(f"Expected: {expected_result}")
    print(f"Actual:   {result.sword_type}")
    assert actual_err is None
    assert result.sword_type == expected_result
