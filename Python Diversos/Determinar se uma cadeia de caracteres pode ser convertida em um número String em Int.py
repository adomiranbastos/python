#Determinar se uma cadeia de caracteres pode ser convertida em um número

#valor1= int(input('Valor 1: '))
#valor2= int(input('Valor 2: '))
#sum= valor1 + valor2
#print("Soma:" + str(sum))


#A função isnumeric() retorna um valor booliano se o valor de cadeia de caracteres pode ser convertido em um valor numérico.

#Adicionar um código que usa a função isnumeric() para determinar se uma cadeia de caracteres pode ser convertida em um número

valor_numerico = '7'
print(valor_numerico.isnumeric())

valor_string = 'Bob'
print(valor_string.isnumeric())

x= 'Abc123#1245'
print(x.isalnum()) #Verifica se a cadeia de caracteres não tem caracteres especiais, como %, $, #, @ ou !.

print(x.isalpha()) #Verifica se a cadeia de caracteres contém apenas letras do alfabeto.

print(x.isdecimal()) #Verifica se a cadeia de caracteres contém apenas valores decimais (números).

print(x.istitle()) #Verifica se a cadeia de caracteres segue as regras de uso de maiúsculas (como em uma frase).

print(x.isupper()) #Verifica se a cadeia de caracteres contém apenas letras maiúsculas.

print(x.islower()) #Verifica se a cadeia de caracteres contém apenas letras minúsculas.