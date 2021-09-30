import math

def test_getNumbers():
    """
    Checks the getNumbers function
    """
    assert formatter.getNumbers("some chars and $10.00") == 10.0
    assert formatter.getNumbers("some chars and $10.99 some other chars") == 10.99
    assert formatter.getNumbers("") == math.inf