

#calculadora 

print('Calculadora simples!')

valor1 = input('Insira o primeiro número: ')

if valor1.isnumeric() == False:
    print('Insira somente números.')
    exit()

operacao = input('Insira a Operação matemática: ')

valor2 = input('Insira o segundo número: ')

if valor2.isnumeric() == False:
    print('Insira somente números..')
    exit()

valor1 = int(valor1)
valor2 = int(valor2)

resultado = 0
if operacao == '+':
    resultado = valor1 + valor2
    label = 'Soma'
elif operacao == '-':
    resultado = valor1 - valor2
    label = 'Subtração'
elif operacao == '*':
    resultado = valor1 * valor2
    label = 'Multiplicação'
elif operacao == '/':
    resultado = valor1 / valor2
    label = 'Divisão'
elif operacao == '**':
    resultado = valor1 ** valor2
    label = 'Exponente'
elif operacao == '%':
    resultado = valor1 % valor2
    label = 'modulus'
else:
    print('Operação não reconhecida.')
    exit()

print(label + ' de ' + str(valor1) + ' ' + operacao + ' ' + str(valor2) + ' é igual a: ' + str(resultado))

# subtracao = valor1 - valor2
# multiplicacao = valor1 * valor2
# divisao = valor1 + valor2

# resto = valor1 % valor2 
# #Você deseja determinar se um número é dividido de maneira uniforme em outro número. Qual operador você usará? %

# expoente = valor1 ** valor2
#print(valor1) operacao (valor2)



