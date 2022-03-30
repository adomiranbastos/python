import random
roll = random.randint(1,60)
print(f'Número aleatorio {roll}.')

import random as alias
roll = alias.randint(0, 60)
print(f'Número aleatorio {roll}')

import random as dice
roll = dice.randint(1, 10)
print(f'You rolled {roll}')