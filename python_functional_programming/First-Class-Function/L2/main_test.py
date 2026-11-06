import pytest
from main import file_type_getter

run_cases = [
    pytest.param(
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".doc",
        "document",
    ),
    pytest.param(
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".png",
        "image",
    ),
]

submit_cases = [
    pytest.param(
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".txt",
        "Unknown",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        [("code", [".py", ".js"]), ("markup", [".html", ".xml"])],
        ".js",
        "code",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("file_extension_tuples", "ext", "expected"), run_cases + submit_cases
)
def test_file_type_getter(file_extension_tuples, ext, expected):
    print("\n---------------------------------")
    print("Input tuples:")
    for file_type, extensions in file_extension_tuples:
        print(f"  {file_type}: {extensions}")
    print(f"Extension: {ext}")
    print(f"Expected: {expected}")
    try:
        getter_function = file_type_getter(file_extension_tuples)
        result = getter_function(ext)
    except Exception as error:
        result = f"Error: {error}"
    print(f"Actual:   {result}")
    assert result == expected
