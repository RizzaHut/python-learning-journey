import pytest
from main import add_format, remove_format

run_cases = [
    pytest.param(
        {"docx": True, "pdf": True},
        "add_format",
        add_format,
        "txt",
        {"docx": True, "pdf": True, "txt": True},
    ),
    pytest.param(
        {"md": True, "txt": False},
        "add_format",
        add_format,
        "ppt",
        {"md": True, "txt": False, "ppt": True},
    ),
    pytest.param(
        {"md": True, "txt": False},
        "remove_format",
        remove_format,
        "md",
        {"md": False, "txt": False},
    ),
]

submit_cases = [
    pytest.param(
        {},
        "add_format",
        add_format,
        "docx",
        {"docx": True},
        marks=pytest.mark.submit,
    ),
    pytest.param(
        {"docx": True, "pdf": True, "txt": False},
        "remove_format",
        remove_format,
        "pdf",
        {"docx": True, "pdf": False, "txt": False},
        marks=pytest.mark.submit,
    ),
    pytest.param(
        {"docx": True, "pdf": True, "txt": False},
        "add_format",
        add_format,
        "jpg",
        {"docx": True, "pdf": True, "txt": False, "jpg": True},
        marks=pytest.mark.submit,
    ),
    pytest.param(
        {"docx": False, "pdf": True, "txt": True},
        "add_format",
        add_format,
        "docx",
        {"docx": True, "pdf": True, "txt": True},
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("default_formats", "formatter_name", "formatter", "new_format", "expected"),
    run_cases + submit_cases,
)
def test_formatters(default_formats, formatter_name, formatter, new_format, expected):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * default_formats: {default_formats}")
    print(f" * formatter: {formatter_name}")
    print(f" * new_format: {new_format}")
    print(f"Expected: {expected}")
    input_copy = default_formats.copy()
    result = formatter(default_formats, new_format)
    print(f"Actual:   {result}")
    assert result == expected
    if default_formats != input_copy:
        print("default_formats was mutated!")
    assert default_formats == input_copy
