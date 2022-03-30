#No primeiro exemplo, os campos de substituição não têm nenhum valor dentro deles. Usando o operador de acesso de membro, 
# chamamos a função format(). 
# Passamos os valores que desejamos substituir em cada campo de substituição na ordem em que eles aparecem.

#medicamento = 'Glicose'
#dosagem = 5
#duracao = 4.5
#
#bula = '{} - Tomar {} ML a cada {} horas'.format(medicamento, dosagem, duracao) #aqui segue a ordem correta pois não tem valores nas chaves
#print(bula)
#
#bula = '{2} - Tomar {1} ML a cada {0} horas'.format(medicamento, dosagem, duracao) #duração será a posição 2 pois começa do zero
#print(bula)
#
#bula = '{medicamento} - Tomar {dosagem} ML a cada {duracao} horas'.format(medicamento = 'Bezetacil', dosagem = 10, duracao = 6) #aqui se usou os nomes 
#
#print(bula)

#código para usar literais de cadeia de caracteres formatados ou "f-strings"

#nome = 'Mundo'
#mensagem = f'Olá, {nome}.'
#print(mensagem)
#
#contar = 10
#valor = 3.14
#mensagem = f'Count para {contar}.  multiplicar por {valor}.'
#print(mensagem)

#largura = 5
#altura = 10
#print(f'O perimetro é de {(2 * largura) + (2 * altura)} e a área é {largura * altura}.')


#código para definir especificadores de formato para controlar o alinhamento e o preenchimento

valor = 'Olá'

print(f'.{valor:<25}.')
print(f'.{valor:>25}.')
print(f'.{valor:^25}.')
print(f'.{valor:-^25}.')

#Um especificador de formato usa um símbolo de dois-pontos (:) 
#após o nome da variável para especificar como esse valor deve ser formatado.


