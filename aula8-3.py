# Limpeza de dados

import pandas as pd

df = pd.read_csv('clientes.csv')
print(df.head())

# Remover dados
df.drop('pais', axis=1, inplace=True) # Coluna
df.drop(2, axis=0, inplace=True) # Linha

# Normalizar campos de texto
df['nome'] = df['nome'].str.title() # colocando no formato "Title Case", onde a primeira letra de cada palavra é maiúscula e as demais são minúsculas.
# Se você quiser garantir que todos os valores sejam strings antes de aplicar .title(), pode usar:
# df['nome'] = df['nome'].astype(str).str.title()
# .str.lower(): Converte todos os caracteres para minúsculo
df['endereco'] = df['endereco'].str.lower()
# .str.strip(): Remove espaços em branco (incluindo tabs e quebras de linha) no início e no final de cada string na coluna 'endereco'.
# Exemplo: " SP " → "SP"
# .str.upper(): Converte todos os caracteres para MAIÚSCULOS
df['estado'] = df['endereco'].str.strip().str.upper() 
# OBS: Se 'endereco' contiver valores não-string (como NaN), esses valores serão mantidos como estão (a menos que você use .astype(str) antes)

# Converter tipos de dados
df['idade'] = df['idade'].astype(int) # convertento para número inteiro
# (float) - número com casa decimal
# (str) - texto

# Tratar valores nulos (ausentes)
df_fillna = df.fillna(0) # Substitui valores nulos por 0
df_dropna = df.dropna() # Remover linhas com pelo menos um NaN
df_dropna4 = df.dropna(thresh=4) # Remover todas as linhas que não possuem pelo menos 4 valores não nulos (ou seja, linhas com 3 ou mais valores NaN são descartadas)
df_dropnaall = df.dropna(how='all') # Remover todas as colunas nulas
df = df.dropna(subset=['cpf']) # Remover linha com CPF nulo
