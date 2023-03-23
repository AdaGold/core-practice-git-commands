import pytest


def always_returns_true():
    var = "This is a change!"
<<<<<<< HEAD
    return False
    list = ["tomato", "balloon"]
=======
    return None  

>>>>>>> 10b0a03de82ba4911c9786b37e78f94fd5e47680


def test_always_returns_true():
    assert always_returns_true()
