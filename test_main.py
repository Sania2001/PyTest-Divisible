import main
import pytest


# def input():
#     a = 25
#     return a
@pytest.mark.parametrize("num, output",[(5,True),(2,False),(10,True),(7,False)])
def test_five(num, output):
    # a = 10
    result = main.five(num)
    assert result == output

@pytest.mark.parametrize("num1, output1",[(5,True),(10,True)])
def test_five2(num1, output1):
    # a = 9
    result = main.five(num1)
    assert result == output1

@pytest.mark.parametrize("num, output",[(5,True),(2,False),(10,True),(7,False)])
def test_seven(num, output):
    # b = 49
    result1 = main.seven(num)
    assert result1 == output

@pytest.mark.parametrize("num, output",[(5,True),(2,False),(10,True),(7,False)])
def test_seven2(num, output):
    # b = 50
    result1 = main.seven(num)
    assert result1 == output

@pytest.mark.parametrize("num, output",[(5,True),(2,False),(10,True),(7,False)])
def test_nine(num, output):
    #c = 81
    result2 = main.nine(num)
    assert result2 == output

@pytest.mark.parametrize("num, output",[(5,True),(2,False),(10,True),(7,False)])
def test_nine2(num, output):
    #c = 82
    result2 = main.nine(num)
    assert result2 == output

@pytest.mark.parametrize("num, output",[(5,True),(2,False),(10,True),(7,False)])
def test_eleven(num, output):
    #d = 121
    result3 = main.eleven(num)
    assert result3 == output

@pytest.mark.parametrize("num, output",[(11,True),(121,False),(22,True),(33,False)])
def test_eleven2(num, output):
    # d = 122
    result3 = main.eleven(num)
    assert result3 == output