import pytest
from main import convert_file_format

run_cases = [
    pytest.param("Proposal.docx", "pdf", "Proposal.pdf"),
    pytest.param("Invoice.txt", "md", "Invoice.md"),
]

submit_cases = [
    pytest.param(
        "Presentation.ppt", "pptx", "Presentation.pptx", marks=pytest.mark.submit
    ),
    pytest.param("Intro.pptx", "jpeg", None, marks=pytest.mark.submit),
    pytest.param("Summary.md", "txt", "Summary.txt", marks=pytest.mark.submit),
    pytest.param("Contract.pdf", "pdoof", None, marks=pytest.mark.submit),
]


def mutate_globals():
    convert_file_format.__globals__["valid_extensions"] = [
        "docx",
        "txt",
        "pptx",
        "ppt",
        "md",
    ]
    convert_file_format.__globals__["valid_conversions"] = {
        "docx": ["jpeg"],
        "pdf": ["docx", "txt", "md"],
        "txt": ["docx"],
        "ppt": ["pptx", "jpeg"],
        "md": ["png"],
        "jpeg": ["png"],
    }


@pytest.mark.parametrize(("name", "ext", "expected"), run_cases + submit_cases)
def test_convert_file_format(name, ext, expected):
    print("\n---------------------------------")
    mutate_globals()
    print("Inputs:")
    print(f" * filename: {name}")
    print(f" * target_format: {ext}")
    print(f"Expected: {expected}")
    result = convert_file_format(name, ext)
    print(f"Actual:   {result}")
    assert result == expected
