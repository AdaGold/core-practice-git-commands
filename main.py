import pytest
#changes

def always_returns_true():
    
    # true always return True
    return True


def test_always_returns_true():
    assert always_returns_true()
