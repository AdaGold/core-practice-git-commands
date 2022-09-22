import pytest


def always_returns_true():
    print("Hi Irene!")
    print("GitHub is cool!")
    return True


def test_always_returns_true():
    assert always_returns_true()
