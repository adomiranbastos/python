valor1 = '  FIRST challenge         '
valor2 = '-  second challenge  -'
valor3 = 'tH IR D-C HALLE NGE'

valor4 = 'fourth'
valor5 = 'fifth'
valor6 = 'sixth'

# First challenge
valor1 = valor1.strip()
valor1 = valor1.lower()
valor1 = valor1.title()
valor1 = f'{valor1:^30}'

# Second challenge
valor2 = valor2.replace('-', '')
valor2 = valor2.strip()
valor2 = valor2.capitalize()

# Third challenge
valor3 = valor3.replace(' ', '')
valor3 = valor3.replace('-', ' ')
valor3 = valor3.swapcase()
valor3 = f'{valor3:>30}'

print(valor1)
print(valor2)
print(valor3)

# Fourth challenge - use only the print() function (no f-strings)
print(valor4, valor5, valor6, sep='#', end='!')

# Fifth challenge - use only a single print() function. Create tabs and new lines using f-strings.
print(f'\n\t{valor4}\n\t{valor5}\n\t{valor6}')