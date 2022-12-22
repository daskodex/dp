"""
         *1
        ***3
       *****5
      *******7
     *********9
    ***********
123*************
12***************
1*****************
"""

import random

def grow_tree(h: int = 10) -> None:
    branch = 1
    for i in range(0, h):
        branch_gen = branch * "*"
        star_position = random.randint(0, branch-1)
        real_branch_gen = ''

        if i != 0:
            real_branch_gen = branch_gen[:star_position] + '0' + branch_gen[star_position+1:]
        else:
            real_branch_gen = '❆'

        print((h-i)*" ", real_branch_gen, sep='')
        branch += 2


    for i in range(0, 2):
        print(((branch // 2)-(branch // 4 // 2)) * " ",  (branch // 4) * "|", sep='')


    return None


grow_tree(10)
