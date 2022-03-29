# 0-Criando diretorio de trabalho C:/FIEC_FAPB/
import os
if not os.path.exists("C:/FIEC_FAPB/"):
    os.makedirs("C:/FIEC_FAPB/")
#obs para o codigo rodar corretamte o arquivo python ProjetoFinal.py
#deverá está drento do diretório criado acima
"""
#1-fazendo o download dos arquivos
import wget
wget.download('http://web.antaq.gov.br/Sistemas/ArquivosAnuario/Arquivos/2019.zip', 'Anuario2019.zip')
wget.download('http://web.antaq.gov.br/Sistemas/ArquivosAnuario/Arquivos/2020.zip', 'Anuario2020.zip')
wget.download('http://web.antaq.gov.br/Sistemas/ArquivosAnuario/Arquivos/2021.zip', 'Anuario2021.zip')
import shutil


#2-descompactar arquivos anuarios
import wget
import shutil
shutil.unpack_archive("Anuario2019.zip")
shutil.unpack_archive("Anuario2020.zip")
shutil.unpack_archive("Anuario2021.zip")

#3-renomeando arquivos para csv atracacao
import os
import shutil
file_oldname = os.path.join("C:/FIEC_FAPB/", "2019Atracacao.txt")
file_newname_newfile = os.path.join("C:/FIEC_FAPB/", "2019Atracacao.csv")
newFileName=shutil.move(file_oldname, file_newname_newfile)
file_oldname = os.path.join("C:/FIEC_FAPB/", "2020Atracacao.txt")
file_newname_newfile = os.path.join("C:/FIEC_FAPB/", "2020Atracacao.csv")
newFileName=shutil.move(file_oldname, file_newname_newfile)
file_oldname = os.path.join("C:/FIEC_FAPB/", "2021Atracacao.txt")
file_newname_newfile = os.path.join("C:/FIEC_FAPB/", "2021Atracacao.csv")
newFileName=shutil.move(file_oldname, file_newname_newfile)
file_oldname = os.path.join("C:/FIEC_FAPB/", "2019Carga.txt")
file_newname_newfile = os.path.join("C:/FIEC_FAPB/", "2019Carga.csv")
newFileName=shutil.move(file_oldname, file_newname_newfile)
file_oldname = os.path.join("C:/FIEC_FAPB/", "2020Carga.txt")
file_newname_newfile = os.path.join("C:/FIEC_FAPB/", "2020Carga.csv")
newFileName=shutil.move(file_oldname, file_newname_newfile)
file_oldname = os.path.join("C:/FIEC_FAPB/", "2021Carga.txt")
file_newname_newfile = os.path.join("C:/FIEC_FAPB/", "2021Carga.csv")
newFileName=shutil.move(file_oldname, file_newname_newfile)
"""
#criando dataframes com os arquivos Atracacao_2019a2021
import pandas as pd
df1 = pd.read_csv("C:/FIEC_FAPB/2019Atracacao.csv", sep=';', encoding='utf8')
df2 = pd.read_csv("C:/FIEC_FAPB/2020Atracacao.csv", sep=';', encoding='utf8')
df3 = pd.read_csv("C:/FIEC_FAPB/2021Atracacao.csv", sep=';', encoding='utf8')

#selecionar colunas de 0 a 16
df1 = df1.iloc[:, 0:16]
df2 = df1.iloc[:, 0:16]
df3 = df1.iloc[:, 0:16]

#juntantando corretamente todas as planilhas de Atracacao_2019a2021
dftotal=pd.concat([df1,df2,df3])
#gerando arquivo unico csv das Atracacao_2019a2021
dftotal.to_csv("atracacao_fato.csv", sep=';', encoding="utf8") 


#criando dataframes com os arquivos Carga_2019a2021
import pandas as pd
df4 = pd.read_csv("C:/FIEC_FAPB/2019Carga.csv", sep=';', encoding='utf8',low_memory=False)
df5 = pd.read_csv("C:/FIEC_FAPB/2020Carga.csv", sep=';', encoding='utf8',low_memory=False)
df6 = pd.read_csv("C:/FIEC_FAPB/2021Carga.csv", sep=';', encoding='utf8',low_memory=False)

#selecionar colunas de 0 a 16
df4 = df4.iloc[:, 0:16]
df5 = df5.iloc[:, 0:16]
df6 = df6.iloc[:, 0:16]

#juntantando corretamente todas as planilhas de Carga_2019a2021
dftotal2=pd.concat([df4,df5,df6])
#gerando arquivo unico csv das Carga_2019a2021
dftotal2.to_csv("carga_fato.csv", sep=';', encoding="utf8") 


# as consultas nos arquivos gerados foram utilizando o power query do excel

