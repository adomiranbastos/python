# Initiate an empty list
list1 = []
# OR
list1 = list()

# Initiate a list with elements
list2 = ['hello', 'hola', 'olá']

"" "
Oselementos da lista NÃO precisam ser iguais tipo, mas isso é incomum. 
Neste caso, cada lista pode representar uma série de informações sobre uma pessoa, 
mas você precisará se lembrar quais informações estão armazenadas em cada índice. ---> Existe uma opção melhor para este propósito - dicionário. 
"" " 
list3 = ["John", "male", 20, False]

# Accessing information stored in the list by position ("index")
# Note: in CS, first position is ALWAYS 0
print("First element in list2 : "+ list2[0])
print("Second element in list2 : "+ list2[1])

list2.insert(1,'hallo')
list2[1]
print(list2)
list2.append('bye')
list2
print(list2)
list2.remove('hello')
list2
print(list2)
list2.append("hello")
list2.pop()
list2
print(list2)
list2.sort()
list2
print(list2)

print("size of list1 = " + str(len(list1)))
print("size of list2 = " + str(len(list2)))

print (" , ".join(list2))

lists = []
lists.append([1,2,3])
lists.append(['a','b','c'])
print(lists)

lists
print(lists[1])
print(lists[1][0])


