def five(a):
    if a % 5 ==0:
        return True
    else:
        return False

def seven(a):
    if a % 7 ==0:
        return True
    else:
        return False

def nine(a):
    if a % 9 ==0:
        return True
    else:
        return False

def eleven(a):
    if a % 11 ==0:
        return True
    else:
        return False

if __name__ == "__main__":
    num1 = int(input("Enter a number"))
    result1 = five(num1)
    result2 = seven(num1)
    result3 = nine(num1)
    result4 = eleven(num1)

    print(result1)
    print(result2)
    print(result3)
    print(result4)