import pytest


def always_returns_true():
    var = "This is a change!"
    return False
    list = ["tomato", "balloon"]


def test_always_returns_true():
    assert always_returns_true()
