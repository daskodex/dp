"""
Задание:

1.Нужно красиво отформатировать вывод данных на экран [+]
2.Вывести имя самого взрослого или самого молодого участника [+]
3.Выбрать 3х случайных победителей конкурса и вывести их имена и возраст [+]
4.Процедуру вывода, сделать в виде красивой анимации в консоли [+]
"""

import random
import time

def add_separate_and_print(mans_info, max_name_length=15, max_age_length=4) -> None:
    full_name = mans_info[0] + (" " * (max_name_length - len(mans_info[0])))
    full_age = mans_info[1] + (" " * (max_age_length - len(mans_info[1])))

    print(f'{full_name}{full_age}')

    return None


with open('users_list.txt', 'r', encoding="utf-8") as f:
    u_list = f.read().splitlines()

print(f'Успешно считали файл из {len(u_list)} строк\n')

full_user_list = []

for s in u_list:
    full_user_list.append(s.split(" "))

max_age_name = ''
max_age = 0

min_age_name = ''
min_age = 100

for man in full_user_list:
    if int(man[1]) > max_age:
        max_age_name = man[0]
        max_age = int(man[1])

    if int(man[1]) < min_age:
        min_age_name = man[0]
        min_age = int(man[1])

print(f'Самый взрослый это "{max_age_name}" с возрастом {max_age} лет')
print(f'Самый молодой это "{min_age_name}" с возрастом {min_age} лет')

print(f'\nСписок участников из {len(full_user_list)} человек:')

for man in full_user_list:
    add_separate_and_print(man)

# красивая анимация

for i in range(0, 50):
    print(f'\rРобот выбирает участника: { i * "|" }',end = '')
    time.sleep(0.05)

print('\n')

winner_list = []
i = 0

print('\nКонкурс состоялся, победители:')
while len(winner_list) < 3:
    x = random.randint(0, len(full_user_list)-1)
    if not (x in winner_list):
        i += 1
        winner_list.append(x)
        print(f'Победитель {i}: {full_user_list[x][0]} его возраст {full_user_list[x][1]} лет')

