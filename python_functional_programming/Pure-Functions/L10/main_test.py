import pytest
from main import (
    add_custom_command,
    add_format,
    add_line_break,
    default_commands,
    default_formats,
    save_document,
    saved_documents,
)

run_cases = [
    pytest.param(
        ("add_format", add_format),
        default_formats,
        [("rtf",), ("csv",)],
        ["txt", "md", "html", "rtf", "csv"],
    ),
    pytest.param(
        ("save_document", save_document),
        saved_documents,
        [
            ("My_Princess_Diaries.txt", "I can't be a princess!"),
            (
                "The_Devil_Wears_Boots.md",
                "Please, bore someone else with your questions.",
            ),
        ],
        {
            "My_Princess_Diaries.txt": "I can't be a princess!",
            "The_Devil_Wears_Boots.md": "Please, bore someone else with your questions.",
        },
    ),
    pytest.param(
        ("add_line_break", add_line_break),
        "It's not you, it's me.",
        [()],
        "It's not you, it's me.\n\n",
    ),
]

submit_cases = [
    pytest.param(
        ("add_format", add_format),
        default_formats,
        [("doc",), ("docx",), ("pdf",)],
        ["txt", "md", "html", "doc", "docx", "pdf"],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ("save_document", save_document),
        saved_documents,
        [
            ("Function_Club.txt", "The types you own end up owning you"),
            ("Shrek.doc", "Functions are like onions."),
        ],
        {
            "Function_Club.txt": "The types you own end up owning you",
            "Shrek.doc": "Functions are like onions.",
        },
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ("add_line_break", add_line_break),
        "Go be free.",
        [()],
        "Go be free.\n\n",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("command", "initial", "command_calls", "expected"), run_cases + submit_cases
)
def test_custom_command(command, initial, command_calls, expected):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * new command: {command[0]}")
    print(f" * starting input: {initial}")
    result = initial
    commands = default_commands
    initial_copy = initial.copy() if hasattr(initial, "copy") else initial
    default_commands_length = len(default_commands)
    commands = add_custom_command(commands, *command)
    for args in command_calls:
        if len(args) > 0:
            print(f" * input: {args}")
        result = commands[command[0]](result, *args)
    print(f"Expected: '{expected}'")
    print(f"Actual:   '{result}'")
    assert result == expected
    if initial != initial_copy:
        print("Starting input modified")
    assert initial == initial_copy
    if len(default_commands) != default_commands_length:
        print("default_commands modified")
    assert len(default_commands) == default_commands_length
