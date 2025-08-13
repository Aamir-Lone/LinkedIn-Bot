def check_content_safety(text: str) -> bool:
    """
    Very basic safety check.
    In production, integrate with moderation APIs.
    """
    banned_words = ["spam", "fake", "scam"]
    return not any(word in text.lower() for word in banned_words)
