import pytest
from main import restore_documents

run_cases = [
    pytest.param(
        (
            ("Mortgage", "Marriage Certificate", "Boot.dev Certificate"),
            ("VEHICLE TITLE", "MORTGAGE"),
        ),
        {"MORTGAGE", "MARRIAGE CERTIFICATE", "BOOT.DEV CERTIFICATE", "VEHICLE TITLE"},
    ),
    pytest.param(
        (
            ("ANNUITY", "WATER BILL"),
            ("Photo Album", "1235023451345", "Year Book"),
        ),
        {"ANNUITY", "WATER BILL", "PHOTO ALBUM", "YEAR BOOK"},
    ),
]

submit_cases = [
    pytest.param(((), ()), set(), marks=pytest.mark.submit),
    pytest.param(
        (
            ("RECEIPT FOR 1st AND LAST RENT", "School Loan"),
            ("SCOOTER REGISTRATION", "314159", "ENGLISH MAJOR DEGREE"),
        ),
        {
            "RECEIPT FOR 1ST AND LAST RENT",
            "SCHOOL LOAN",
            "SCOOTER REGISTRATION",
            "ENGLISH MAJOR DEGREE",
        },
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("inputs", "expected"), run_cases + submit_cases)
def test_restore_documents(inputs, expected):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * original documents: {inputs[0]}")
    print(f" * backup documents: {inputs[1]}")
    print(f"Expected: {expected}")
    try:
        result = restore_documents(*inputs)
    except Exception as error:
        result = f"Error: {error}"
    print(f"Actual:   {result}")
    assert result == expected
