#entrada do teclado usando uma instrução if e a função isnumeric()
#Combinar isnumeric() com uma instrução if

valor1 = input('Valor1: ')

if valor1.isnumeric() == False:
    print('Valor1 não é númerico')
    exit()

valor2 = input('Valor2: ')

if valor2.isnumeric() == False:
    print('Valor2 não é númerico')
    exit()
valor1 = int(valor1)
valor2 = int(valor2)

sum = valor1 + valor2
print('Soma: ' + str(sum))

