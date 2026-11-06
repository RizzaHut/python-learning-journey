import pytest
from main import join_first_sentences

run_cases = [
    pytest.param(
        ["I don't feel safe", "Are you cussing with me"],
        2,
        "I don't feel safe. Are you cussing with me.",
    ),
    pytest.param(
        ["You're fantastic", "He's just another rat", "Where'd the food come from"],
        2,
        "You're fantastic. He's just another rat.",
    ),
]

submit_cases = [
    pytest.param(["I'm not different"], 0, "", marks=pytest.mark.submit),
    pytest.param(
        [
            "You wrote a bad song",
            "This is a good idea",
            "Just buy the tree",
            "It's going to flood",
            "Tell us what to do",
            "Here comes the train",
            "Are you cussing with me?",
            "This is just cider",
            "Get me a bandit hat",
        ],
        3,
        "You wrote a bad song. This is a good idea. Just buy the tree.",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("input_sentences", "input_n", "expected"), run_cases + submit_cases
)
def test_join_first_sentences(input_sentences, input_n, expected):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * sentences: {input_sentences}")
    print(f" * n: {input_n}")
    print("Expected:")
    print(f" * {expected}")
    result = join_first_sentences(input_sentences, input_n)
    print("Actual:")
    print(f" * {result}")
    assert result == expected
