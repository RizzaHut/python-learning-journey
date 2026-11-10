import pytest
from main import remove_emphasis

run_cases = [
    pytest.param("*Don't* panic.\n", "Don't panic.\n"),
    pytest.param(
        "The **answer to the ultimate question** of life, the universe and everything is *42*\n",
        "The answer to the ultimate question of life, the universe and everything is 42\n",
    ),
    pytest.param(
        "For a moment, *nothing* happened.\nThen, after a second or so, nothing **continued** to happen.\n",
        "For a moment, nothing happened.\nThen, after a second or so, nothing continued to happen.\n",
    ),
]

submit_cases = [
    pytest.param("", "", marks=pytest.mark.submit),
    pytest.param(
        "The Hitchhiker's Guide is a d*mn **useful** book.\n",
        "The Hitchhiker's Guide is a d*mn useful book.\n",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "In the beginning the *universe* was created.\nThis has made a lot of people very *angry* and been widely regarded as a bad move.\n",
        "In the beginning the universe was created.\nThis has made a lot of people very angry and been widely regarded as a bad move.\n",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "Ford, you're turning into a *penguin*\n",
        "Ford, you're turning into a penguin\n",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "*Space* is big.\nYou just won't **believe** how vastly, hugely, mind-bogglingly big it is.\n",
        "Space is big.\nYou just won't believe how vastly, hugely, mind-bogglingly big it is.\n",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "***Life before death, journey before destination.***\n",
        "Life before death, journey before destination.\n",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input_doc", "expected"), run_cases + submit_cases)
def test_remove_emphasis(input_doc, expected):
    print("\n---------------------------------")
    print(f"Input document:\n{input_doc}")
    print(f"Expected output:\n{expected}")
    try:
        result = remove_emphasis(input_doc)
    except Exception as error:
        result = f"Exception raised: {error}"
    print(f"Actual output:\n{result}")
    assert result == expected
