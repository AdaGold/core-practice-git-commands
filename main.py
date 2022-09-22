import pytest

CAT_COLORS = ["orange", "tabby", "black", "white", "gray", "calico"]

def always_returns_true():
    print("I love my cat Percy!")
    print("Percy is soft and fluffy")
    
    
    
    print("How old is Percy?")
    print("I wonder if Percy would be friends with my cat Bodhi!")
    
    print("Percy would cower in fear")
    return True

def kitty_power():
    for cat in CAT_COLORS:
        print(cat)

def test_always_returns_true():
    assert always_returns_true()



    print("Surprise! I changed this line!")
