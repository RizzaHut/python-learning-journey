import pytest
from main import pair_document_with_format

run_cases = [
    pytest.param(
        (["Proposal", "Invoice", "Contract"], ["docx", "pdoof", "txt"]),
        [("Proposal", "docx"), ("Contract", "txt")],
    ),
    pytest.param(
        (["Presentation", "Summary"], ["pptx", "docx"]),
        [("Presentation", "pptx"), ("Summary", "docx")],
    ),
]

submit_cases = [
    pytest.param(([], []), [], marks=pytest.mark.submit),
    pytest.param(
        (["Test", "Example"], ["ppt", "docx"]),
        [("Test", "ppt"), ("Example", "docx")],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        (
            ["Python Cheatsheet", "Java Cheatsheet", "Malware", "Golang Cheatsheet"],
            ["pdf", "docx", "trash", "docx"],
        ),
        [
            ("Python Cheatsheet", "pdf"),
            ("Java Cheatsheet", "docx"),
            ("Golang Cheatsheet", "docx"),
        ],
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("inputs", "expected"), run_cases + submit_cases)
def test_pair_document_with_format(inputs, expected):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * doc_names: {inputs[0]}")
    print(f" * doc_formats: {inputs[1]}")
    print(f"Expected: {expected}")
    try:
        result = pair_document_with_format(*inputs)
    except Exception as error:
        result = f"Error: {error}"
    print(f"Actual:   {result}")
    assert result == expected
