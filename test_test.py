# SPDX-License-Identifier: MIT
"""Tests for test module."""
import test


def test_add():
    assert test.add(1, 2) == 3
    assert test.add(0, 0) == 0
    assert test.add(-1, 1) == 0


def test_greet():
    assert test.greet("World") == "Hello, World!"
    assert test.greet("BCOS") == "Hello, BCOS!"