# Dictionary= Dicionário uma estrutura de dados que armazena pares de valores-chave nos quais as chaves DEVEM ser objetos imutáveis.
dict={}

dict2 = {'a': 5, 'b':10, 'c':100, 'd': 9.5}
print(dict2['b']) 

#atualização de valores
dict2['b']=50
print(dict2['b']) 

# Os valores no dicionário podem ser misturados 
# Vejamos um exemplo com dict {}, um dicionário vazio iniciado acima. 
# Primeiro, inseriremos alguns pares de chave / valor no programa. 

dict [ "saudação" ]  =  "mensagem de olá" 
dict [ "alfabeto" ]  =  [ 'a' ,  'b' ,  'c' ,  'd' ,  'e' ] 
dict [ "check-in" ]  =  False 
dict [ "phoneNumber" ]  =  8007782346 

print(dict)

# Mas como a tupla é imutável, poderíamos substituir a lista por uma tupla 
dict['a','b', 'c'] = [False, True, False]
print(dict)
# Também podemos recuperar todas as chaves 
print(dict.keys())
# Ou todos os valores 
print(dict.values())
# Elementos em um dicionário também podem ser retornados como um par. 
print(dict.items())



