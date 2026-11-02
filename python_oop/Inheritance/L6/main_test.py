import pytest
from main import Archer, Wizard

run_cases = [
    (
        Wizard("Ron", 50, 90),
        Archer("Odysseus", 80, 2),
        ["shoot", "shoot", "shoot", "cast"],
        [None, None],
        "not enough arrows",
    ),
    (
        Wizard("Harry", 30, 70),
        Archer("Pericles", 100, 3),
        ["cast", "shoot", "shoot"],
        [10, 75],
        None,
    ),
]

submit_cases = [
    pytest.param(
        Wizard("Luna", 65, 49),
        Archer("Paris", 85, 2),
        ["cast", "shoot", "shoot", "cast"],
        [None, None],
        "not enough mana",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        Wizard("Neville", 55, 45),
        Archer("Hector", 75, 3),
        ["shoot", "cast"],
        [45, 50],
        None,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("wizard", "archer", "actions", "expected_result", "expected_err"),
    run_cases + submit_cases,
)
def test_actions(wizard, archer, actions, expected_result, expected_err):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * Wizard: {wizard.get_name()}, HP: {wizard.get_health()}")
    print(f" * Archer: {archer.get_name()}, HP: {archer.get_health()}")
    print(f"Actions: {actions}")
    print()

    try:
        for action in actions:
            if action == "cast":
                print(f"{wizard.get_name()} casts a spell at {archer.get_name()}")
                wizard.cast(archer)
            elif action == "shoot":
                print(f"{archer.get_name()} shoots an arrow at {wizard.get_name()}")
                archer.shoot(wizard)
        print()
        wizard_hp = wizard.get_health()
        archer_hp = archer.get_health()
        actual_err = None
    except Exception as error:
        wizard_hp = None
        archer_hp = None
        actual_err = str(error)

    if expected_err is not None or actual_err is not None:
        print(f"Expected Exception: {expected_err}")
        print(f"Actual Exception:   {actual_err}")
        assert actual_err == expected_err
        return

    print(f"Expected Wizard HP: {expected_result[0]}")
    print(f"Actual Wizard HP:   {wizard_hp}")
    print(f"Expected Archer HP: {expected_result[1]}")
    print(f"Actual Archer HP:   {archer_hp}")
    assert actual_err is None
    assert [wizard_hp, archer_hp] == expected_result
