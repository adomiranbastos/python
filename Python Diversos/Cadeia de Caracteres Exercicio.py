#usar funções auxiliares de cadeia de caracteres

#A função capitalize() garante que o primeiro caractere em uma cadeia de caracteres esteja em letra maiúscula. 
# Somente a primeira letra da cadeia de caracteres é maiúscula. 
# Se a cadeia de caracteres contiver várias palavras separadas por caracteres vazios, apenas o primeiro caractere estará em letra maiúscula.

#mensagem = str.capitalize('primeira mensagem')
#print(mensagem)

#mensagem = 'segunda mensagem'.capitalize()
#print(mensagem)

#mensagem = 'terceira mensagem'
#print(mensagem.capitalize())


#há funções que alteram as letras maiúsculas para minúsculas ou vice-versa.
#mensagem = 'Olá Mundo'
#print(mensagem.lower())
#print(mensagem.upper())

#mensagem = mensagem.title()
#print(mensagem)
#print(mensagem.swapcase())

#código que conta o número de vezes que uma cadeia de caracteres é encontrada em outra

#localizacao = 'Foz do Iguaçu'
#print (localizacao.count('u'))

#E se você quiser saber quantos caracteres há em uma cadeia de caracteres? 
# Nesse caso, use um método chamado len(). Observe que esse não é um método auxiliar na forma como o definimos, 
# pois funciona em mais do que apenas os valores de cadeia de caracteres.

#print(len('Quantos caracteres existem na palavra?'))

#Chame as funções startswith() e endswith() para inspecionar o conteúdo de uma cadeia de caracteres para descobrir
#se ela corresponde àquilo com que você esperava que ela começasse ou terminasse, respectivamente.

#mensagem = 'casamento'
#print(mensagem.startswith('c')) #inicia com a c?
#print(mensagem.startswith('a')) #inicia com a a?
#print(mensagem.startswith('ca'))#inicia com a ca
#
#print(mensagem.endswith('r'))#terminan com a r?
#print(mensagem.endswith('a'))#terminan com a a?
#print(mensagem.endswith('to'))#terminan com a to?

#mensagem = 'O comando print vai contar a posição das letras nessa mensagem'
#print(mensagem.find('o')) # se encontra na terceira posição pois começa no zero (0)
#print(mensagem.find('t')) # Se encontra na decima terceira posição (13)
#print(mensagem.find('s')) # Se encontra na trigessima casa (30)

#o código que retira caracteres vazios da esquerda ou direita ou de ambos os sentidos

#menssagem = '    centro     '
#print('.' + menssagem.lstrip() + '.')
#print('.' + menssagem.rstrip() + '.')
#print('.' + menssagem.strip() + '.')

#Aqui, concatenamos uma cadeia de caracteres literal que contém um símbolo de ponto (.) antes e depois da variável mensagem e a chamada para uma das funções de remoção. 
#Isso permite que você veja como ele afeta o conteúdo da cadeia de caracteres.

#código que substitui uma cadeia de caracteres encontrada em outra cadeia de caracteres

#mensagem = 'Eu não quero você'
#mensagem = mensagem.replace('não quero', 'quero')
#print(mensagem)

#código que justifica uma cadeia de caracteres adicionando caracteres de espaço vazio
#Os métodos rjust() e ljust() adicionam caracteres de espaço vazio a uma cadeia de 
#caracteres para justificar à direita ou à esquerda, respectivamente.

#mensagem = 'Meu Amor'
#print(mensagem.rjust(20))
#print(mensagem.rjust(20, '-'))#ajusta a direita
#print(mensagem.ljust(20))
#print(mensagem.ljust(20, '-'))#ajusta a esquerda











