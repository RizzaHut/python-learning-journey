import pytest
from main import change_bullet_style

run_cases = [
    pytest.param("* Alai\n- Dink Meeker\n", "* Alai\n* Dink Meeker\n"),
    pytest.param(
        "* Ender Wiggin\n- Petra Arkanian\n* Bean\n",
        "* Ender Wiggin\n* Petra Arkanian\n* Bean\n",
    ),
    pytest.param(
        "- Fly Molo - Dragon Army\n- Carn Carby - Rabbit Army\n* Ambul - Rabbit Army\n",
        "* Fly Molo - Dragon Army\n* Carn Carby - Rabbit Army\n* Ambul - Rabbit Army\n",
    ),
]

submit_cases = [
    pytest.param(
        "- Bonzo Madrid\n- Stilson\n- The Formics\n- Peter Wiggin\n- Valentine Wiggin\n- Colonel Graff\n",
        "* Bonzo Madrid\n* Stilson\n* The Formics\n* Peter Wiggin\n* Valentine Wiggin\n* Colonel Graff\n",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input_document", "expected"), run_cases + submit_cases)
def test_change_bullet_style(input_document, expected):
    print("\n---------------------------------")
    print("Input document:")
    print(input_document)
    print("Expected output:")
    print(expected)
    result = change_bullet_style(input_document)
    print("Actual output:")
    print(result)
    if expected.endswith("\n") and not result.endswith("\n"):
        print("Reason: expected newline at the end of the output")
    assert result == expected
