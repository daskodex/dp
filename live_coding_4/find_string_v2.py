def find_string(sub_str, main_string: str) -> bool:
    if len(sub_str) > len(main_string):
        return False

    index = 0
    for s in sub_str:
        if s in main_string[index:]:
            index = main_string.index(s, index)
        else:
            return False
    else:
        return True


print(find_string('abe', 'atkbce'))



#тесты
assert find_string('abe', 'atkbce') == True
assert find_string('ab', 'atkbce') == True
assert find_string('ab', 'atkce') == False
assert find_string('abe', 'btkace') == False
assert find_string('abe', 'aabbtkacee') == True
assert find_string('abe', 'aa') == False