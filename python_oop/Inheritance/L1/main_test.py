import pytest
from main import Archer, Human

run_cases = [
    ("Faramir", "Human", None),
    ("Bard", "Archer", 1),
]

submit_cases = [
    pytest.param("Boromir", "Human", None, marks=pytest.mark.submit),
    pytest.param("Aragorn", "Human", None, marks=pytest.mark.submit),
    pytest.param("Legolas", "Archer", 93828, marks=pytest.mark.submit),
]


def test_inheritance():
    print("\n---------------------------------")
    print("Inheritance Test:")
    assert issubclass(Archer, Human), "Archer is not a child class of Human"
    print("Archer is a child class of Human")


@pytest.mark.parametrize(("name", "unit_type", "num_arrows"), run_cases + submit_cases)
def test_unit(name, unit_type, num_arrows):
    print("\n---------------------------------")
    print(f"Type:   {unit_type}")
    print(f"Name:   {name}")
    if unit_type == "Archer":
        print(f"Arrows: {num_arrows}")
    print()
    if unit_type == "Human":
        human = Human(name)
        print(f"Expecting name: {name}")
        print(f"Actual name:    {human.get_name()}")
        assert human.get_name() == name
    else:
        assert num_arrows is not None
        archer = Archer(name, num_arrows)
        print(f"Expecting name:   {name}")
        print(f"Actual name:      {archer.get_name()}")
        print(f"Expecting arrows: {num_arrows}")
        print(f"Actual arrows:    {archer.get_num_arrows()}")
        assert (archer.get_name(), archer.get_num_arrows()) == (name, num_arrows)
