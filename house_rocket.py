
#importação das bibliotecas utilizadas no projeto
import pandas as pd

#Criação da variável que armazena os dados da base utilizada para o desafio.
dados_tratados = pd.read_csv("kc_house_data.csv", nrows=50, usecols=["id", "date", "price","yr_built", "yr_renovated"])
tabela = pd.read_csv("kc_house_data.csv", nrows=50)
print(tabela)
print(dados_tratados)