import ast
import inspect
import textwrap
from collections.abc import Callable

import pytest
from main import choose_parser

run_cases = [
    pytest.param("md", "markdown"),
    pytest.param("txt", "plaintext"),
]

submit_cases = [
    pytest.param("markdown", "markdown", marks=pytest.mark.submit),
    pytest.param("MD", "markdown", marks=pytest.mark.submit),
    pytest.param("docx", "plaintext", marks=pytest.mark.submit),
]


def get_ast(fn: Callable[..., object]) -> ast.Module:
    src = textwrap.dedent(inspect.getsource(fn))
    return ast.parse(src)


def uses_ternary(fn: Callable[..., object]) -> bool:
    tree = get_ast(fn)
    fn_def = next(node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
    has_ifexp = any(isinstance(node, ast.IfExp) for node in ast.walk(fn_def))
    has_if_stmt = any(isinstance(node, ast.If) for node in ast.walk(fn_def))
    return has_ifexp and not has_if_stmt


@pytest.mark.parametrize(("input_ext", "expected"), run_cases + submit_cases)
def test_choose_parser(input_ext, expected):
    print("\n---------------------------------")
    if not uses_ternary(choose_parser):
        print("Please use a ternary expression!")
    assert uses_ternary(choose_parser)
    print("Ternary expression detected!")
    print(f"File extension: {input_ext}")
    print(f"Expected parser: {expected}")
    result = choose_parser(input_ext)
    print(f"Chosen parser: {result}")
    assert result == expected
