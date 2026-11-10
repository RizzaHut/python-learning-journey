def convert_case(text: str, target_format: str) -> None:
    if not text or not target_format:
        raise ValueError("no text or target format provided")

    if target_format == "uppercase":
        print(text.upper())
        return
    if target_format == "lowercase":
        print(text.lower())
        return
    if target_format == "titlecase":
        print(text.title())
        return
    raise ValueError(f"unsupported format: {target_format}")
