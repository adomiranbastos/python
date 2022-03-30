import math

# Power function
print("2^5 = " + str(math.pow(2,5)))

# Ceiling function
print(math.ceil(3.45))

print(math.ceil(10.01))

# Floor function
print(math.floor(5.25))

print(math.floor(11.01))

# Absolute Value
print(math.fabs(-10.33))

print(math.fabs(5.25))

# Log with base e, or natural log
print(math.log(1000))

# Log with a specified base of 10
print(math.log(1000,10))

#Análise de dados com Numpy, Matplotlib, Scipy

"""
Numpy é um pacote para computação numérica em python.

Ele fornece uma estrutura de dados eficiente para matrizes numéricas n-dimensionais (ndarray)
Suporta operações de vetor e matriz.

Numpy é implementado em C, por isso é muito rápido e eficiente.
O tipo de dados básico em numpy é o array n-dimensional numpy. 
Eles podem ser usados ​​para representar vetores (1D), matrizes (2D) ou tensores (nD).

Matrizes numpy de dimensões 1 são freqüentemente usadas para representar uma série de dados.
As matrizes n-dimensionais geralmente representam conjuntos de dados completos (cada coluna é um tipo de medida).
Matrizes Numpy são muito semelhantes às listas Python. 

A indexação e o fatiamento funcionam da mesma maneira (incluindo classificações). No entanto , 
todas as células na mesma matriz devem conter o mesmo tipo de dados.
Os operadores não funcionam da mesma forma para listas e matrizes e há muitos métodos adicionais definidos neles."""

#Vetores e matrizes são coleções de variáveis contínuas na memória e acessadas através de um número de índice. 
#A diferença entre vetores e matrizes é que vetores são de uma única dimensão, # enquanto matrizes podem conter várias dimensões.

# Let's see what happen if we use a list to represent a vector?
print([1,2,3] * 3)

# Previous was NOT the expected output with vector multiplication by a scalar

# Need to do this
print([i*3 for i in [1,2,3]])

# What about summing two vectors?
# Treated as list concatenation
print([1,2,3]+[4,5,6])

# Sum two vectors
a = [1,2,3]
b = [4,5,6]
print([a[i] + b[i] for i in range(len(a))])

# cross product or dot product?
#print([1,2,3] * [4,5,6]) #maneira errada 


# We could compute the dot product like this:

u = [1,2,3]
v = [4,5,6]

total = 0 
for i in range(len(u)):
    total += u[i] * v[i]
print(total)

# Let's see what happens if we use Numpy

# np is a common convention to refer to numpy throughout the code
import numpy as np 
u = np.array([1,2,3])
v = np.array([4,5,6])

# dot() calculates the dot product of two vectors
print(np.dot(u,v))
print(type(u))
print(type(v))
print(u)


# Mais algumas operações em arrays 1D: 

import  numpy  as  np 
u  =  np . array ([ 1 , 2 , 3 ]) 
v  =  np . array ([ 4 , 5 , 6 ]) 

print( "Adição de vetor com outro vetor --->"  +  str ( u + v )) 
print( "Adição de vetor com uma escalar --->"  +  str ( u + 4 )) 
print("Multiplicação do vetor por um escalar --->"  +  str ( u  *  4 )) 
print( "Multiplicação do vetor (NÃO ponto nem produto cruzado) --->"  +  str ( u  *  v )) 
print( "Soma do vetor ---> "  +  str ( np.sum ( u  *  v ))) 
print( " Produto  escalar ---> " +  str ( np.dot ( u , v )))


# Return the shape/dimension of array
print(u.shape)

print(np.ones((2,3)))

print(np.ones((3, 2)))