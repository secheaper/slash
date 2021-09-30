"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the XYZ license with
this file. If not, please write to: secheaper@gmail.com

"""
import formatter
import math

def test_getNumbers():
    """
    Checks the getNumbers function
    """
    assert formatter.getNumbers("some chars and $10.00") == 10.0
    assert formatter.getNumbers("some chars and $10.99 some other chars") == 10.99
    assert formatter.getNumbers("") == math.inf