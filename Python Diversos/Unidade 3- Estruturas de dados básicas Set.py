#Set = Definir =Conjunto : uma estrutura de dados mutável que armazena objetos não duplicados 
# e imutáveis ​​e classifica os elementos em ordem crescente.Cada elemento do conjunto é único.
# #Desenvolvimento Back-end Python Manipulando sets no Python: 
# Os sets são uma coleção de itens desordenada, parcialmente imutável e que não podem conter elementos duplicados. 
# Por ser parcialmente imutável, os sets possuem permissão de adição e remoção de elementos.
novoset= set()
novoset

ex1= {1,2,2,1,1}
print(ex1) #mostra os numeros sem repetição e em ordem crescente

ex2 = {j for j in range(10)}
print(ex2)

ex2.add(2)
ex2.add(10)
ex2.add(50)
print(ex2) #ira adicionar somente o 10 e 50, pois os outro elemento já existe (2)

idade = [10, 5, 4, 5, 2, 1, 5] # transformar uma lista em Set 
definir_idade = set(idade)

print(definir_idade)

#Tipos imutáveis não suportam modificações, daí o nome imutável. 
# Então, quando tipos imutáveis são alterados (concatenação de string, por exemplo), 
# o Python retornará uma nova instância de um objeto de string para ser atribuído a um nome de variável.

