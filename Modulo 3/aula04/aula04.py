'''
aula 04: análise de dados
dataset: OCORRENCIAS_2025.CSV
'''

# importar biblioteca
import pandas as pd
import os

# criar o dataframe
# Padrão do csv é separar por ",". sep muda o parâmetro para ";"
# encoding força a compreensão de caracteres como `´~
df = pd.read_csv('OCORRENCIAS_2025.csv', sep=';', encoding='latin-1')

os.system('cls')
# ver apenas as 5 primeiras linhas
print(df.head())

# shape mostra quantos registros e quantas colunas tem o dataset
print(df.shape())

# ver as colunas do dataset
print(df.columns)

#--------------------------------------------------------------------#

# Analisar dados / kpi's

# 1 - Qual o total de ocorrências registradas?
totalOcorrencias = df['TOTAL'].sum()
print(f'\nTotal de Ocorrências Registradas em 2025: {totalOcorrencias}\n')

# 2 - Quantas ocorrências de cada tipo foi registrada?
verOcorrecias = df['TIPO_OCORRENCIA'].value_counts()
print(verOcorrecias)

# 3 - Qual o tipo de ocorrência mais comum?
verOcorrecias = df['TIPO_OCORRENCIA'].value_counts().idxmax()
print(f'\nO tipo de ocorrência mais comum é {verOcorrecias}\n')

# Número de ocorrência por Estado?
#   sort_values ordena por quantidade
#   sort_index ordena em ordem alfabética
qtdeOcorrenciaUF = df.groupby('UF')['TOTAL'].sum().sort_index()
print(qtdeOcorrenciaUF)
