valor1 = 2
valor2 = 5
valor_verdeiro = True
valor_falso = False

if valor2 > 1 and valor1 < 10:
    print('O Valor está entre 1 e 10.')

if valor1 > 1 or valor2 > 1:
    print('Valores maiores que 1')

print(not valor_verdeiro)
print(not valor_falso)

if not valor1 > 1 and valor2 < 10:
    print('Valor passou no teste')
else:
    print('Valores não passaram no teste')