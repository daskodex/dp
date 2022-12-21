def find_string(sub_str, main_string: str) -> bool:
    if len(sub_str) > len(main_string):
        return False

    counter = 0
    s = main_string
    for i in range(0, len(sub_str)):
        if sub_str[i] in s:
            s = s[i+1:]
            counter += 1
        else:
            return False

    if counter >= len(sub_str):
        return True
    else:
        return False


print(find_string('abe', 'atkbce'))



#тесты
assert find_string('abe', 'atkbce') == True
assert find_string('ab', 'atkbce') == True
assert find_string('ab', 'atkce') == False
assert find_string('abe', 'btkace') == False
assert find_string('abe', 'aabbtkacee') == True
assert find_string('abe', 'aa') == False