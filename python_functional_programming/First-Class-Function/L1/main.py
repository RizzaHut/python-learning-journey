from collections.abc import Callable
    

def file_to_prompt(
    file: dict[str, str], to_string: Callable[[dict[str, str]], str]
) -> str:
    converted_file: str = to_string(file) 
    formatted_prompt: str = f"```\n{converted_file}\n```"
    return formatted_prompt
