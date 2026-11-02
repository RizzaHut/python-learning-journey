import pytest
from main import Dragon, Unit

run_cases = [
    (
        [Unit("Cian", 3, 3), Unit("Andrew", -1, 4), Unit("Baran", -6, 5)],
        Dragon("Draco", 2, 2, 3),
        2,
        3,
        ["Cian", "Andrew"],
    ),
]

submit_cases = [
    pytest.param(
        [
            Unit("Carbry", 2, 1),
            Unit("Yvor", 1, 0),
            Unit("Eoin", 2, 0),
            Unit("Edwin", 10, 10),
        ],
        Dragon("Fafnir", 1, 1, 1),
        1,
        1,
        ["Carbry", "Yvor", "Eoin"],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [Unit("Nicholas", 0, 1), Unit("Andrew", -1, 4), Unit("Baran", -6, 5)],
        Dragon("Hydra", 0, 0, 2),
        0,
        1,
        ["Nicholas"],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [
            Unit("Yvor", 1, 0),
            Unit("Nicholas", 0, 1),
            Unit("Eoin", 2, 0),
            Unit("Cian", 3, 3),
            Unit("Andrew", -1, 4),
            Unit("Baran", -6, 5),
            Unit("Carbry", 2, 1),
        ],
        Dragon("Smaug", 6, 6, 2),
        1,
        1,
        ["Yvor", "Nicholas", "Eoin", "Cian", "Carbry"],
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("units", "dragon", "x_target", "y_target", "expected_hit_units"),
    run_cases + submit_cases,
)
def test_breathe_fire(units, dragon, x_target, y_target, expected_hit_units):
    print("\n---------------------------------")
    print(f"{dragon.name} breathes fire at ({x_target}, {y_target})")
    for unit in units:
        print(f"  - {unit.name} is at ({unit.pos_x}, {unit.pos_y})")
    print()
    print("Expecting to hit:")
    for unit in expected_hit_units:
        print(f"  - {unit}")
    hit_units = dragon.breathe_fire(x_target, y_target, units)
    hit_unit_names = [unit.name for unit in hit_units]
    print("Actually hit:")
    for unit in hit_units:
        print(f"  - {unit.name}")
    assert set(hit_unit_names) == set(expected_hit_units)
