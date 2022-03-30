#código para usar o operador lógico or

valor1 = input('Valor1: ')
valor2 = input('Valor2: ')

if valor1.isnumeric() == False or valor2.isnumeric() == False:
    print('Insira somente números')
    exit()


valor1 = int(valor1)
valor2 = int(valor2)

sum = valor1 + valor2
print('Soma: ' + str(sum))



