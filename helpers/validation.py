def validate_name(name):
    """Validate the user's name."""
    if len(name) > 20:
        return False
    # Allow only alphanumeric and common symbols
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~ "
    return all(c in allowed_chars for c in name)