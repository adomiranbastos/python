

#calculadora a mina maneira
valor1=input('Insira o valor 1: ')
if valor1.isnumeric() ==False:
    print('Insira somente números')
    exit()
operacao= input('Escolha qual a operação matemática + (soma) - (subtração) * (multiplicação): ')
valor2=input('Insira o valor 2: ')
if valor2.isnumeric() ==False:
    print('Insira somente números')
    exit()
    
valor1= int(valor1)
valor2= int(valor2)
 
if operacao == ('+'):
    sum = (valor1 + valor2)
   
    print('Resultado da Soma é: ' + str(sum))
 
elif operacao == ('-'):
    subtracao = (valor1 - valor2)
    print('Resultado da Subtração é: ' + str(subtracao)) 
 
elif operacao == ('*'):
     multiplicacao = (valor1 * valor2)
     print('Resultado da multiplicação é: ' + str(multiplicacao)) 

else:
     operacao != ('*') or ('+') or ('-')
     print('insira uma operação correta')
 
 #if operacao != ('+') or ('-') or ('*')):
  #       print('escolha uma operação incorreta (+ , - , ou *)')


# subtracao = valor1 - valor2
# multiplicacao = valor1 * valor2
# divisao = valor1 + valor2
# resto = valor1 % valor2
# expoente = valor1 ** valor2
#print(valor1) operacao (valor2)



