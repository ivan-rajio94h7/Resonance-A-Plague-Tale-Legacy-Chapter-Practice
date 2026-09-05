# Build: 253530d62b8134f88b11a7fdfffad0c8

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
