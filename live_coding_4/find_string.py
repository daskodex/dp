def find_string(sub_str, main_string: str) -> bool:
    if len(sub_str) > len(main_string):
        return False

    counter = 0
    s = main_string
    for i in range(0, len(sub_str)):
        if sub_str[i] in s:
            s = s[i + 1:]
            counter += 1
        else:
            return False

    if counter >= len(sub_str):
        return True
    else:
        return False


if __name__ == '__main__':

# тесты
    assert find_string('abe', 'atkbce')
    assert find_string('ab', 'atkbce')
    assert find_string('abe', 'aabbtkacee')

    assert not find_string('abe', 'aa')
    assert not find_string('ab', 'atkce')
    assert not find_string('abe', 'btkace')

