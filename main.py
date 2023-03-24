import pytest


def always_returns_true():
    # true always return true
    #comment addedgit
    return True


def test_always_returns_true():
    assert always_returns_true()
