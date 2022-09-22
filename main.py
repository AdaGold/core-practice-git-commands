import pytest


def always_returns_true():
    print("I love my cat Percy!")
    print("Percy is soft and fluffy")
    return True


def test_always_returns_true():
    assert always_returns_true()
