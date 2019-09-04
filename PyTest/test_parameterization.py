import pytest

def sum(a, b):
    return a+b

@pytest.mark.parametrize("input1, input2, output",
                         [
                             (19, 6, 25),
                             (6, 3, 9),
                             (5, 5, 10)
                         ]
                         )

def test_sum1(input1, input2, output):
    result = sum(input1,input2)
    assert result == output

"""
def test_sum1():
    result = sum(19,6)
    assert result == 25

def test_sum2():
    result = sum(6,3)
    assert result == 9

def test_sum13():
    result = sum(5,5)
    assert result == 10
"""