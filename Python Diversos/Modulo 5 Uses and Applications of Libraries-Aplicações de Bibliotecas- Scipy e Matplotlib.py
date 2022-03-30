#Scipy é um pacote para analisar o ajuste da curva.
#Matplotlib é um pacote para dados gráficos.
#Veja a seguir um exemplo de como scipy, numpy e matplotlib podem ser usados ​​juntos na análise de dados.

# import diferentes pacotes usados ​​para análise de dados 
# .. "as opt" significa que o programador pode usar a abreviação de "opt" para se referir a esta biblioteca, 
# em vez de digitar o nome completo 
import  scipy.optimize  as  opt 
import  numpy  as  np 
import  matplotlib.pyplot  as  plt 


# Dados brutos inseridos manualmente pelo usuário 
I =[4.0, 3.5, 3.0, 2.5, 2.0]
B =[1.31, 1.14, 0.97 ,0.81, 0.76]
IError = [0.2, 0.2, 0.2, 0.2, 0.2]
BError = [0.03, 0.02, 0.04, 0.02, 0.05]

print ( "B estimado para cada erro \ n " ) 
for i in range  (5): 
    print(str ( I [ i ])  +  "+ -"  +  str (IError [ i ])  +  ":"  +  str ( B [ i ])  +  "+ -"  +  str ( BError [ i ])) 

# Aplique a biblioteca Numpy para formatar a lista de dados brutos em uma matriz multidimensional 
# Isto é necessário para a otimização da função e para usar adequadamente o pacote Scipy   

xdata = np.array(I)
ydata = np.array(B)
xerror = np.array(IError)
yerror= np.array(BError)


# Define a função linear para ajuste, 
def  func ( h ,  m ,  b ): 
    return  m * h  +  b 


# w dá o parâmetro estimado para m e b, armazenado na matriz quadrada de w e u 
# o que falta _ retornar informações sobre variância e covariância 

# w é uma matriz com informações sobre o valor da inclinação e da interceptação y 
w ,  u  =  opt . curve_fit ( func , xdata ,  ydata )  

# Aplique as coordenadas x e o resultado otimizado sobre o ajuste da curva para encontrar a "Linha do Melhor Ajuste" 
yfit  =  func ( xdata , * w ) 
    
# Use o pacote Matplotlib para representar graficamente os dados 
  # 1. Faça o gráfico das barras de erro para cada x -valor 
  # 2. Represente graficamente a "Linha de melhor ajuste" 

# Nota: existem opções para personalizar a aparência do seu gráfico com diferentes parâmetros 
plt.errorbar(I, B, xerr=IError, yerr = BError, fmt='o', ms = 3)
plt.plot(xdata,yfit,label="Fit", linewidth=1.5, linestyle='dashed')

# Adicionar título e rótulos ao gráfico 

plt.title('I vs. B of the Electromagnet')
plt.xlabel('Electromagnet Current I (A)')
plt.ylabel('Magnetic Field B (T)')


print("\n Estimated parameters of m and b: ", w)
print("\n Estimated variance of m & b: ", np.sqrt(np.diag(u)))

# Se necessário, é assim que você pode salvar o gráfico para sua máquina local. 
# Mas aqui NÃO precisamos salvar o gráfico, então comentaremos esta linha. 

# Especifique o nome da imagem como o parâmetro 
#plt.savefig ('Adomiran.jpg') 

# Observação: se você estão mostrando e armazenando o gráfico, certifique-se de SAVE antes de SHOW. 
plt . show ()