def validate_title(title: str) -> str:
    """Validate and normalize a task title."""
    if not isinstance(title, str):
        raise ValueError("Task title must be text.")

    title = title.strip()

    if not title:
        raise ValueError("Task title cannot be empty.")

    if len(title) > 120:
        raise ValueError("Task title must be 120 characters or fewer.")

    return title
