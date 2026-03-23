# SPDX-License-Identifier: MIT
"""Simple test module for BCOS v2 Action verification."""


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("BCOS"))
    print(f"1 + 2 = {add(1, 2)}")