import pytest
from main import word_count_memo

run_cases = [
    pytest.param(
        "My hovercraft is full of eels",
        {
            "My hovercraft is full of eels": 6,
            "He's a lumberjack and he's okay. He sleeps all night and he works all day": 15,
        },
        (
            6,
            {
                "My hovercraft is full of eels": 6,
                "He's a lumberjack and he's okay. He sleeps all night and he works all day": 15,
            },
        ),
    ),
    pytest.param(
        "Spam, spam, spam, spam, spam, spam, baked beans, spam, spam, and spam",
        {},
        (
            12,
            {
                "Spam, spam, spam, spam, spam, spam, baked beans, spam, spam, and spam": 12
            },
        ),
    ),
]

submit_cases = [
    pytest.param(
        "This is an ex-parrot",
        {"This parrot is no more": 5},
        (4, {"This parrot is no more": 5, "This is an ex-parrot": 4}),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "This doc should 'incorrectly' have 9999 words to test that the memoization is working",
        {
            "My hovercraft is full of eels": 6,
            "This doc should 'incorrectly' have 9999 words to test that the memoization is working": 9999,
        },
        (
            9999,
            {
                "My hovercraft is full of eels": 6,
                "This doc should 'incorrectly' have 9999 words to test that the memoization is working": 9999,
            },
        ),
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("input_doc", "input_memos", "expected"), run_cases + submit_cases
)
def test_word_count_memo(input_doc, input_memos, expected):
    print("\n---------------------------------")
    print(f"Input document:\n  {input_doc}")
    print("Input memos:")
    for key, value in input_memos.items():
        print(f"  {key}: {value}")
    print(f"Expected word count: {expected[0]}")
    print("Expected memos:")
    for key, value in expected[1].items():
        print(f"  {key}: {value}")
    input_memos_copy = input_memos.copy()
    result = word_count_memo(input_doc, input_memos_copy)
    print(f"Actual word count: {result[0]}")
    print("Actual memos:")
    for key, value in result[1].items():
        print(f"  {key}: {value}")
    if input_memos_copy != input_memos:
        print("Mutated input memos")
    assert input_memos_copy == input_memos
    if input_memos == expected[1] and result[1] != expected[1]:
        print("Expected word count from the input memos")
    assert result == expected
