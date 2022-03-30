
#código que executa várias operações matemáticas no novo arquivo de código

# valor1 = 5
# valor2 = 4
# 
# sum = valor1 + valor2
# subtracao = valor1 - valor2
# multiplicacao = valor1 * valor2
# divisao = valor1 + valor2
# resto = valor1 % valor2
# expoente = valor1 ** valor2
# 
# print('Soma: ' +str(sum))
# print('Subtração: ' + str(subtracao))
# print('Multiplicação: ' + str(multiplicacao))
# print('Divisão: ' + str(divisao))
# print('Resto: ' + str(resto))
# print('Expoente: ' + str(expoente))


#+: operador de adição
#-: operador de subtração
#*: operador de multiplicação
#/: operador de divisão
#%: operador de módulo, que fornece o resto (se houver) após a divisão de um valor por outro. É útil saber se um valor é divisível de maneira uniforme pelo outro.
#**: operador de expoente. Por exemplo, "5 elevado à quarta potência" é expresso como 5 * 5 * 5 * 5.

# print(3 + 4 * 5)
# print((3 + 4) * 5)
# P arênteses: resolva primeiro as operações entre parênteses.
# E xponentes: resolva os expoentes.
# M ultiplicação: resolva a multiplicação, da esquerda para a direita.
# D ivisão: resolva a divisão, da esquerda para a direita.
# A dição: resolva a adição, da esquerda para a direita.
# S ubtração: resolva a subtração, da esquerda para a direita

#código para investigar a divisão mais de perto
# valor1=5
# valor2=4# 

# divisao= valor1/valor2
# print(type(divisao))
# print(divisao)

# valor1 = 3.14
# print(type(valor1))
# print(int(valor1))
# 
# valor2 = 99.99
# print(type(valor2))
# print(int(valor2))

#valor1= round(7.654321, 2)
#print(valor1)

#valor2= round(9.87654, 3)
#print(valor2)

#Converter a temperatura de Fahrenheit em Celsius

fahrenheit = input('Qual a temperatura em Fahrenheit?  ')

if fahrenheit.isnumeric() == False:
    print('Insira somente números.')
    exit()

fahrenheit = int(fahrenheit)

celsius = int((fahrenheit - 32) * 5/9)
print('A temperatura em Celsus é: ' + str(celsius))






