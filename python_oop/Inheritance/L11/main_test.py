import pytest
from main import BatteringRam, Catapult, Siege

run_cases = [
    (Siege(100, 10), 100, 4, 40, None),
    (BatteringRam(100, 10, 2000, 5), 100, 5, 70, 10),
    (Catapult(100, 10, 2), 100, 6, 60, 2),
]

submit_cases = [
    pytest.param(Siege(60, 5), 100, 2, 40, None, marks=pytest.mark.submit),
    pytest.param(
        BatteringRam(80, 5, 2000, 4), 100, 4, 100, 8, marks=pytest.mark.submit
    ),
    pytest.param(Catapult(90, 4, 3), 100, 10, 250, 3, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    (
        "vehicle",
        "distance",
        "food_price",
        "expected_cost",
        "expected_cargo_volume",
    ),
    run_cases + submit_cases,
)
def test_trip(vehicle, distance, food_price, expected_cost, expected_cargo_volume):
    vehicle_type = vehicle.__class__.__name__
    actual_cost = int(vehicle.get_trip_cost(distance, food_price))
    actual_cargo_volume = vehicle.get_cargo_volume()
    if actual_cargo_volume is not None:
        actual_cargo_volume = int(actual_cargo_volume)
    print("\n---------------------------------")
    print(f"Testing {vehicle_type}")
    print(f" * Max Speed:  {vehicle.max_speed} kph")
    print(f" * Efficiency: {vehicle.efficiency} km/food")
    print(f"Expected Cargo Volume: {expected_cargo_volume}")
    print(f"Actual Cargo Volume:   {actual_cargo_volume}")
    print()
    print("Inputs:")
    print(f" * Distance: {distance} km")
    print(f" * Price: {food_price} per food")
    print(f"Expected Trip Cost: {expected_cost} ")
    print(f"Actual Trip Cost:   {actual_cost}")
    assert (actual_cost, actual_cargo_volume) == (
        expected_cost,
        expected_cargo_volume,
    )
