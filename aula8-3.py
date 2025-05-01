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

print(df.info()) # para enxergar infos (se não é nulo e o tipo de dado) por coluna 

print('Valores nulos: \n', df.isnull().sum()) # para enxergar infos (se não é nulo e o tipo de dado) por coluna 

print('Qtd de registros nulos com fillna:', df_fillna.isnull().sum().sum()) # Resultado: Imprime o total de valores NaN restantes em df_fillna
print('Qtd de registros nulos com dropna:', df_dropna.isnull().sum().sum()) # Resultado: Imprime o total de valores NaN restantes em df_dropna
print('Qtd de registros nulos com dropna4:', df_dropna4.isnull().sum().sum()) # Resultado: Imprime o total de valores NaN restantes em df_dropna4
print('Qtd de registros nulos com CPF:', df['cpf'].isnull().sum()) # Resultado: Imprime o total de valores NaN restantes na coluna CPF
print('Qtd de registros nulos do DF:', df.isnull().sum().sum()) # Resultado: Imprime o total de valores NaN do DataFrame

# Continuação: Tratar valores nulos (ausentes)
df.fillna({'estado': 'Desconhecido', 'bairro': 'Não informado'}, inplace=True) # Substitui os valores nulos na coluna 'estado' por 'Desconhecido' e da coluna 'bairro' por 'Não informado'
# inplace=True: Modifica o DataFrame df diretamente, sem precisar criar uma nova variável. Se fosse inplace=False (padrão), você precisaria atribuir a um novo DataFrame. Segue exemplo abaixo:
# df_novo = df.fillna({'estado': 'Desconhecido', 'bairro': 'Não informado'})
df['endereco'] = df['endereco'].fillna('Endereço não informado') # Substitui os valores NaN da somente da coluna 'endereco' por 'Endereço não informado'.
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean()) # Cria uma nova coluna chamada 'idade_corrigida' no DataFrame (ou seja, não modifica a coluna original), contendo: Os valores originais de 'idade' (onde não eram NaN). E a média da coluna 'idade' nos lugares onde havia NaN.

# Outra alternativas comuns:
# Preencher todas as colunas com um valor padrão: df.fillna('Desconhecido', inplace=True)
# Preencher com a moda (valor mais frequente): df['estado'].fillna(df['estado'].mode()[0], inplace=True)
# Preencher numéricos com a média: df['idade'].fillna(df['idade'].mean(), inplace=True)
# Preencher com a mediana (menos sensível a outliers): df['idade_corrigida'] = df['idade'].fillna(df['idade'].median())

# Tratar formato de dados (Datas)
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce') # Essa linha de código realiza a conversão de uma coluna de datas em formato texto (string) para o tipo datetime.
# errors='coerce': Se encontrar um valor que não corresponde ao formato (ex.: "31/02/2023" ou "abc"): Converte para NaT (Not a Time, equivalente a NaN para datas). Sem essa opção, o pandas levantaria um erro.
# Substituir NaT por uma data padrão:
df['data_corrigida'].fillna(pd.to_datetime('01/01/1970'), inplace=True)
# Dica adicional: verificar se a conversão foi bem-sucedida: 
# print(df['data_corrigida'].isna().sum())  # Conta quantos valores são NaT (inválidos). # Conta quantos valores são NaT (inválidos).

# Tratar dados duplicados
print('Qtd registros atual: ', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print('Qtd registros removendo as duplicadas: ', len(df))

print('Dados Limpos: \n', df)