import pytest
from main import count_words

run_cases = [
    pytest.param("Functional programming in Python", 4),
    pytest.param("Functions", 1),
]

submit_cases = [
    pytest.param("", 0, marks=pytest.mark.submit),
    pytest.param("  functions   return new values  ", 4, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(("document", "expected"), run_cases + submit_cases)
def test_count_words(document, expected):
    print("\n---------------------------------")
    print(f"Document: {document!r}")
    print(f"Expected: {expected}")
    result = count_words(document)
    print(f"Actual:   {result}")
    assert result == expected
