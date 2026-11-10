def list_files(
    parent_directory: dict[str, dict | None], current_filepath: str = ""
) -> list[str]:
    if not parent_directory:
        return []
    file_paths = []
    for name, content in parent_directory.items():
        new_path = current_filepath + "/" + name
        if content == None:
           file_paths.append(new_path)

        deep_path = list_files(content, new_path)
        file_paths.extend(deep_path)
    return file_paths


