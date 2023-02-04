import this

def reverse(x: int) -> int:
    z = 1 if x >= 0 else -1
    tmp = int(str(abs(x))[::-1])*z

    if not -2**31 < tmp < 2**31 - 1:
        return 0
    else:
        return tmp

if __name__ == '__main__':
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(0) == 0
    assert reverse(1200) == 21
    assert reverse(-1200) == -21