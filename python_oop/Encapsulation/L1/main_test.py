import pytest
from main import Wizard

run_cases = [
    ("Merlin", 10, 10, 1000, 100),
    ("Morgana", 20, 5, 2000, 50),
]

submit_cases = [
    pytest.param("Arthur", 3, 3, 300, 30, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    (
        "wizard_name",
        "wizard_stamina",
        "wizard_intelligence",
        "expected_health",
        "expected_mana",
    ),
    run_cases + submit_cases,
)
def test_encapsulation(
    wizard_name,
    wizard_stamina,
    wizard_intelligence,
    expected_health,
    expected_mana,
):
    print("\n---------------------------------")
    print("Creating wizard with:")
    wizard = Wizard(wizard_name, wizard_stamina, wizard_intelligence)
    print(f"  Name: {wizard.name}")
    print(f"  Stamina: {wizard_stamina}")
    print(f"  Intelligence: {wizard_intelligence}")
    print("After initialization:")
    print(f"  Expected mana: {expected_mana}")
    print(f"  Actual mana:   {wizard.mana}")
    print(f"  Expected health: {expected_health}")
    print(f"  Actual health:   {wizard.health}")
    assert wizard.mana == expected_mana
    assert wizard.health == expected_health

    is_private = True
    if hasattr(wizard, "stamina"):
        is_private = False
        print("Stamina isn't private!")
    if hasattr(wizard, "intelligence"):
        is_private = False
        print("Intelligence isn't private!")

    private_attributes_exist = True
    try:
        getattr(wizard, "_Wizard__stamina")
        getattr(wizard, "_Wizard__intelligence")
    except AttributeError:
        print("Attributes __stamina and __intelligence must exist!")
        private_attributes_exist = False

    assert private_attributes_exist
    assert is_private
