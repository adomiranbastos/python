#As classes são projetos ou modelos ou modelos para instâncias. 
# A relação entre uma classe e uma instância é semelhante àquela entre um cortador de biscoitos e um biscoito.
# Um único cortador(classe) de biscoitos pode fazer qualquer número de biscoitos(instancia).
# O cortador define a forma do biscoito. Os biscoitos são comestíveis, mas o cortador de biscoitos não.
# Referências das palestras ENGI1006 do professor Daniel Bauer da Columbia University

# BibliotecaLivro é o nome dado a classe 
class BibliotecaLivro:

#  A library book= Um livro da biblioteca

  # # pass indica que o corpo / naipe da definição de classe está vazio. 
  pass

meu_livro = BibliotecaLivro()
print(meu_livro)
print(type(meu_livro))

#As classes em Python oferecem todas as características tradicionais da programação orientada a objetos: 
# o mecanismo de herança permite múltiplas classes base (herança múltipla), 
# uma classe derivada pode sobrescrever quaisquer métodos de uma classe ancestral, 
# e um método pode invocar outro método homônimo de uma classe ...

print(isinstance(meu_livro, BibliotecaLivro))

#As classes em Python são elementos que, apesar de não serem obrigatórios, ajudam a otimizar a leitura dos códigos. 
# Elas servem, sobretudo, para agrupar as funções de um determinado objeto dentro da programação de um software, por exemplo


#Data fields - Each instance owns its own data (the class can define what names the data fields have).
#Data fields=Campos de dados - cada instância possui seus próprios dados 
#(a classe pode definir quais nomes os campos de dados têm).



"""
    A BibliotecaLivro.
    """
#The init(self, ...) method is automatically called by Python when a new instance is created. This method is called the class constructor; it initialize the data values in the class.
#O método init (self, ...) é chamado automaticamente pelo Python quando uma nova instância é criada. 
# Esse método é chamado de construtor de classe ; ele inicializa os valores dos dados na classe.
# init, Self Parameter

class BibliotecaLivro (object):   

      """
      O parâmetro self é OBRIGATÓRIO dentro da classe, 
      porque diz ao programa para recuperar / agir na instância do objeto 
      que o chamou.
      """  
def __init__(self, titulo, autor, ano, numero_tel):
          self.titulo = titulo
          self.autor = autor
          self.ano = ano
          self.numero_tel = numero_tel
          self.checked_out = False 
""" 
Uma vez que já criamos meu_livro como um objeto BibliotecaLivro, 
podemos agora adicionar manualmente o título, autor, ... informações associadas ao livro. 
"""

meu_livro . titulo  =  "Sonhos e Visões de Deus" 
meu_livro . autor  =  ( "Adomiran Bastos") 
meu_livro . ano  =  2021
meu_livro . numero_tel  =  "(045) 9121-7974"

print(meu_livro.titulo)
print(meu_livro.autor)
print(meu_livro.ano)
print(meu_livro.numero_tel)


""" 
Ou podemos passar todas as informações para o __init__ para configurar os campos 
ao criar a nova instância. 
"""
#__init__ é o que é chamado como construtor em outras linguagens OOP, como C ++ / Java. 
#A idéia básica é que seja um método especial chamado automaticamente quando um objeto dessa classe é criado.

#a função init ,também chamada de "método construtor", possui a responsabilidade de criar o objeto daquela classe. Nem sempre você precisará cria-lá, porém, se o seu projeto exige que você utilize essa função, nela será contida todas as informações principais do objeto. Um exemplo disso pode ser o objeto "Pessoa":

novo_livro = BibliotecaLivro("Sonhos e Visões de Deus" , "Adomiran Bastos" ,  2021 ,  "(045) 9121-7974")
print(novo_livro.titulo)

#traceback=É o mesmo que stacktrace, um termo um pouco mais usado em linguagens em geral. 
#A tradução literal é rastreamento. Então serve para rastrear o que a aplicação está fazendo, mas de uma forma simples. O código é sempre executado em uma pilha de chamadas de funções, 
#ou seja cada função que é chamada é colocada nessa pilha.
