in_str = '''Абзац (нем. Absatz «раздел, часть текста») — отрезок письменной речи, состоящий из одного или нескольких предложений. Абзац, обозначая своего рода «цезуру», является единицей членения текста, промежуточной между фразой и главой, и служит для группировки однородных единиц изложения, исчерпывая один из его моментов (тематический, сюжетный и т. д.). Выделение фразы в особый абзац усиливает падающий на неё смысловой акцент. Абзац способствует правильному и быстрому восприятию текста.'''

# 1.Англ. или русских букв
# 2.От 2 символов
# 3.Пробел ' '
# 4.Знаки
# 5.Нижний регистр

sub_str = ''
statistic_words_list = []

for s in in_str:
    if s.isalpha() or s == ' ':
        sub_str += s.lower()

words_list = set(sub_str.split(' '))

for s in words_list:
    if len(s) > 1:
        statistic_words_list.append([sub_str.count(s), s])

statistic_words_list.sort(reverse=True)

for i in range(0, len(statistic_words_list)):
    print(f'{statistic_words_list[i][1]} -> {statistic_words_list[i][0]}')


