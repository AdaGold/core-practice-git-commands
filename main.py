import pytest
#changes

def always_returns_true():
    #testing
    # true always return true
    return True


def test_always_returns_true():
    assert always_returns_true()
