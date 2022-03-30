print(type('7')) 
#str : o tipo de dados para cadeias de caracteres. As cadeias de caracteres podem conter todos os caracteres alfanuméricos. 
# Elas podem ser curtas (apenas alguns caracteres) ou muito longas (um parágrafo inteiro de dados textuais).
print(type(7)) 
#int : o tipo de dados para valores inteiros, que pode ser qualquer número não fracionário, positivo ou negativo.
print(type(7.1))
#float : o tipo de dados para valores float, que podem incluir valores fracionários representados como números 
# que incluem um ponto decimal e números após o decimal.

#Em seguida, adicione o código que usa isinstance() para verificar o tipo de dados dos vários valores
print(isinstance('7', str))
print(isinstance(7, int))
print(isinstance(7.1, float))

print(isinstance(7, str))
print(isinstance('7', int))
print(isinstance('7.1', float))

#É possível criar uma expressão booliana usando a função type()? Sim
print(type('7') == str)
print(type(7) == int)
print(type(7.1) == float)

print(type(7) == str)
print(type('7') == int)
print(type('7.1') == float)
