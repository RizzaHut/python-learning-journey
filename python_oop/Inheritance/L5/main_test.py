import pytest
from main import Archer, Hero

run_cases = [
    (("Hercules", 200), ("Pericles", 100, 2), 190, None, False),
    (("Zeus", 1000), ("Hades", 900, 1), None, "not enough arrows", True),
    (("Aquiles", 150), ("Aneas", 80, 1), 140, None, False),
]

submit_cases = [
    pytest.param(
        ("Hecate", 300),
        ("Ares", 50, 0),
        None,
        "not enough arrows",
        True,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ("Icarus", 60),
        ("Daedalus", 40, 2),
        40,
        None,
        True,
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("hero_args", "archer_args", "expected_result", "expected_err", "twice"),
    run_cases + submit_cases,
)
def test_shoot(hero_args, archer_args, expected_result, expected_err, twice):
    hero = Hero(*hero_args)
    archer = Archer(*archer_args)

    print("\n---------------------------------")
    print(f"Hero:   {hero.get_name()}, Health: {hero.get_health()}")
    print(f"Archer: {archer.get_name()}, Arrows: {archer_args[2]}")
    print()
    try:
        print(f"{archer.get_name()} tries to shoot {hero.get_name()}")
        archer.shoot(hero)
        if twice:
            print(f"{archer.get_name()} tries to shoot {hero.get_name()} again")
            archer.shoot(hero)
        result = hero.get_health()
        actual_err = None
    except Exception as error:
        result = None
        actual_err = str(error)

    if expected_err is not None or actual_err is not None:
        print(f"Expected Exception: {expected_err}")
        print(f"Actual Exception:   {actual_err}")
        assert actual_err == expected_err
        return

    print(f"Expected {hero.get_name()} health: {expected_result}")
    print(f"Actual   {hero.get_name()} health: {result}")
    assert actual_err is None
    assert result == expected_result
