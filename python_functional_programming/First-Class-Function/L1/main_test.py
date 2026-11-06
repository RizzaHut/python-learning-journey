import pytest
from main import file_to_prompt


def to_string(file):
    return (
        f"File: {file['filename']}\n"
        f"Author: {file['author_first_name']} {file['author_last_name']}\n"
        f"Content: {file['content']}"
    )


run_cases = [
    pytest.param(
        {
            "filename": "essay.txt",
            "content": "Dear Mr. Vernon, we accept the fact that we had to sacrifice a whole Saturday in detention for whatever it was we did wrong...",
            "author_first_name": "Brian",
            "author_last_name": "Johnson",
        },
        "```\nFile: essay.txt\nAuthor: Brian Johnson\nContent: Dear Mr. Vernon, we accept the fact that we had to sacrifice a whole Saturday in detention for whatever it was we did wrong...\n```",
    ),
    pytest.param(
        {
            "filename": "letter.txt",
            "content": "But we think you're crazy to make us write an essay telling you who we think we are.",
            "author_first_name": "Brian",
            "author_last_name": "Johnson",
        },
        "```\nFile: letter.txt\nAuthor: Brian Johnson\nContent: But we think you're crazy to make us write an essay telling you who we think we are.\n```",
    ),
]

submit_cases = [
    pytest.param(
        {
            "filename": "note.txt",
            "content": "Does Barry Manilow know that you raid his wardrobe?",
            "author_first_name": "John",
            "author_last_name": "Bender",
        },
        "```\nFile: note.txt\nAuthor: John Bender\nContent: Does Barry Manilow know that you raid his wardrobe?\n```",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input_file", "expected"), run_cases + submit_cases)
def test_file_to_prompt(input_file, expected):
    print("\n---------------------------------")
    print("Inputs:")
    print(f"  filename: {input_file['filename']}")
    print(f"  content: {input_file['content'][:30]}...")  # Truncate for display
    print(f"  author_first_name: {input_file['author_first_name']}")
    print(f"  author_last_name: {input_file['author_last_name']}")
    print(f"Expected:\n{expected}")
    result = file_to_prompt(input_file, to_string)
    print(f"Actual:\n{result}")
    assert result == expected
