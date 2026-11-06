from collections.abc import Callable


def file_type_getter(
    file_extension_tuples: list[tuple[str, list[str]]],
) -> Callable[[str], str]:
    file_extension_dict = {}
    for file_type, file_extensions in file_extension_tuples:
        for file in file_extensions:
            file_extension_dict[file] = file_type
    return lambda file: file_extension_dict.get(file, "Unknown")
