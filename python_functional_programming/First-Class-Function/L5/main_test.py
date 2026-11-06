import pytest
from main import remove_invalid_lines

run_cases = [
    pytest.param(
        "\n* We are the music makers\n- And we are the dreamers of dreams\n* Come with me and you'll be\n",
        "\n* We are the music makers\n* Come with me and you'll be\n",
    ),
    pytest.param(
        "\n* In a world of pure imagination\n- There is no life I know\n* Living there - you'll be free\n",
        "\n* In a world of pure imagination\n* Living there - you'll be free\n",
    ),
]

submit_cases = [
    pytest.param(
        "\n* If you want to view paradise\n- Simply look around and view it\n* Anything you want to, do it\n* There is no life I know\n- To compare with pure imagination\n* Living there, you'll be free\n",
        "\n* If you want to view paradise\n* Anything you want to, do it\n* There is no life I know\n* Living there, you'll be free\n",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input_document", "expected"), run_cases + submit_cases)
def test_remove_invalid_lines(input_document, expected):
    print("\n---------------------------------")
    print("Input document:")
    print('"' + input_document + '"')
    print("Expected output:")
    print('"' + expected + '"')
    result = remove_invalid_lines(input_document)
    print("Actual output:")
    print('"' + str(result) + '"')
    if expected.endswith("\n") and not str(result).endswith("\n"):
        print("Reason: expected newline at the end of the output")
    assert result == expected
