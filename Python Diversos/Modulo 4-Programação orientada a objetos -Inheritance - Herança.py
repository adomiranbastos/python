
#Inheritance=Herança 

#A herança nos permite definir uma class que herda todos os métodos e propriedades de outra class. 
# A class pai é a class da qual está sendo herdada , também chamada de class base. 
#A class filha é a class que herda de outra class, também chamada de class derivada.


class PeixePalhaco(object):
    pass

nemo = PeixePalhaco()

print(type(nemo))

print(isinstance(nemo, PeixePalhaco))

#This relationship is called the is-a relationship
#Esse relacionomento é chamado de relacionomento é um

class Animal( object ): 
    pass

class  Vertebrado(Animal): 
    pass

class  Peixe(Vertebrado): 
    pass

class  PeixePalhaco(Peixe): 
    pass

class  TangFish(Peixe): 
    pass

nemo= PeixePalhaco()
print(isinstance(nemo, PeixePalhaco))

print(isinstance(nemo, TangFish))

print(isinstance(nemo, Animal))

print(isinstance(nemo, object))

#Métodos herdados#Por que usar herança? #Cada classe também tem acesso aos atributos de classe da classe pai. 
#Em particular, os métodos definidos na classe pai podem ser chamados em instâncias de seus "descendentes".

class Peixe(Animal):
    def speak(self): 
        return "Blub"

class PeixePalhaco(Peixe):
    pass

class TangFish(Peixe):
    pass

dory=TangFish()

print(dory.speak())

nemo=PeixePalhaco()
print(nemo.speak())


class TangFish(Peixe):
    def speak(self):
        return "Olá, sou uma instância de TangFish."
dory = TangFish()

# this speak() is from the TangFish class
print(dory.speak())

"""
"Olá, sou uma instância de TangFish."

Por outro lado, como a classe PeixePalhaco ainda NÃO 
define o speak (), as instâncias de PeixePalhaco ainda estão usando 
speak () da classe pai de Peixe. 
""" 

nemo = PeixePalhaco()
print(nemo.speak())

print(nemo)


class  PeixePalhaco (Peixe): 
    def  __init__ ( self ,  nome ): 
        self .nome  =  nome 
    def  __str__ ( self ): 
        return  "Um peixe-palhaço conhecido como " + self . nome
nemo  =  PeixePalhaco ( ' Nemo ' ) 

print ( nemo )

#Accessing Variable with Inheritance= Acessando Variável com Herança Em um relacionamento é-um, 
# a classe filha pode acessar os atributos da classe pai se não estiver definido na classe filha, 
# ou substituir o valor de atributo do mesmo atributo existente na classe filha.
#No entanto, se uma instância for definida em um dos níveis da classe-mãe, 
# ela NÃO poderá acessar os atributos definidos em qualquer um dos níveis da classe-filha mais baixa.

#lass Peixe(Vertebrado):
#   
#   # self.nome is not defined in Peixe class, but is defined in the PeixePalhaco class.
#   def __str__(self):
#       return "Olá meu nome é: {}".format(self.nome)
#   
#class PeixePalhaco(Peixe):
#   def __init__(self, nome):
#       self.nome = nome
#       nemo=PeixePalhaco('Nemo')
#       nemo=Peixe()
#    

class  Peixe (Vertebrado): 
    def  __init__ ( self ,  nome ): 
        self . nome  =  nome 

    # self.nome não é definido na classe Peixe, mas é definido na classe PeixePalhaco. 
    def  __str__ ( self ): 
        return  "Olá, meu nome é {} " . format (self.nome) 
    
class  PeixePalhaco (Peixe): 

    def __init__ (self, nome ):
        self.nome  =  nome
    nemo=PeixePalhaco ( "Nemo" ) 

# __str __ () está acessando self.nome da 
#impressão de nível filho ( nemo )
#Ola meu nome é Nemo
    nemo=Peixe ( "Peixe Palhaço" ) 

# __str__ ia acessando o atributo self.nome da classe Peixe 
print ( nemo )
#Olá, meu nome é Peixe Palhaço