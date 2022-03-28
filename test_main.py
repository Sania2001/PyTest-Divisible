import main

def test_five():
    a = 10
    result = main.five(a)
    assert result == True

def test_five2():
    a = 9
    result = main.five(a)
    assert result == False

def test_seven():
    b = 49
    result1 = main.seven(b)
    assert result1 == True

def test_seven2():
    b = 50
    result1 = main.seven(b)
    assert result1 == False

def test_nine():
    c = 81
    result2 = main.nine(c)
    assert result2 == True

def test_nine2():
    c = 82
    result2 = main.nine(c)
    assert result2 == False

def test_eleven():
    d = 121
    result3 = main.eleven(d)
    assert result3 == True

def test_eleven2():
    d = 122
    result3 = main.eleven(d)
    assert result3 == False