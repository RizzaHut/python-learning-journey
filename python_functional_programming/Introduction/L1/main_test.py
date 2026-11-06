import pytest
from main import stylize_title

run_cases = [
    pytest.param(
        """The Importance of FP
Learn how functional programming can change the way you think about code.
Benefits include immutability, simplicity, and composability.""",
        "          The Importance of FP          \n"
        "****************************************\n"
        "Learn how functional programming can change the way you think about code.\n"
        "Benefits include immutability, simplicity, and composability.",
    ),
]

submit_cases = [
    pytest.param(
        """Short Title
Equally short story""",
        "              Short Title               \n"
        "****************************************\n"
        "Equally short story",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        """DocToDoc: A Guide
Understanding the art of document conversion.
We write cool functional code to make it happen.""",
        "           DocToDoc: A Guide            \n"
        "****************************************\n"
        "Understanding the art of document conversion.\n"
        "We write cool functional code to make it happen.",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input_doc", "expected"), run_cases + submit_cases)
def test_stylize_title(input_doc, expected):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * document: {input_doc}\n")
    print(f"Expected:\n{expected}\n")
    result = stylize_title(input_doc)
    print(f"Actual:\n{result}\n")
    assert result == expected
