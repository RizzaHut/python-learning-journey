import pytest
from main import add_prefix

run_cases = [
    pytest.param(
        ("hello there", "sonny", "how ya doing"),
        ("0. hello there", "1. sonny", "2. how ya doing"),
    ),
]

submit_cases = [
    pytest.param(
        ("go", "python", "java", "javascript"),
        ("0. go", "1. python", "2. java", "3. javascript"),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ("boots", "everyone else"),
        ("0. boots", "1. everyone else"),
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input_docs", "expected"), run_cases + submit_cases)
def test_add_prefix(input_docs, expected):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * documents: {input_docs}")
    print(f"Expected: {expected}")
    documents = ()
    try:
        for doc in input_docs:
            documents = add_prefix(doc, documents)
        result = documents
    except Exception as error:
        result = f"Error: {error}"
    print(f"Actual: {result}")
    assert result == expected
