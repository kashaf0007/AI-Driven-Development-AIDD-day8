import pytest
from app import calculate

def test_add():
    assert calculate("1 + 2") == 3

def test_subtract():
    assert calculate("5 - 2") == 3

def test_multiply():
    assert calculate("3 * 4") == 12

def test_divide():
    assert calculate("10 / 2") == 5

