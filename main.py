import pytest


def always_returns_true():
    var = "This is a change!"
    return True 



def test_always_returns_true():
    assert always_returns_true()
