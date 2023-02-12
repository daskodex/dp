# У вас есть девять цифр: 1, 2, …, 9. Именно в таком порядке.
# Вы можете вставлять между ними знаки «+», «-» или ничего.
# У вас будут получаться выражения вида 123+45-6+7+89.
# Найдите все из них, которые равны 100.


num_list = []
big_list = []
move_list = ['',' ','+','-']

for i in range(1, 6):
    num_list.append(str(i))
    num_list.append(str(i))
num_list.pop(len(num_list)-1)

else:
    print(num_list)


for i in range(1,len(num_list),2):
    for j in move_list:
        pass

    print(num_list[i])



print(num_list)

