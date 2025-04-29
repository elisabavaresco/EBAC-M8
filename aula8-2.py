# Introdução ao tratamento de dados

import pandas as pd

df = pd.read_csv('clientes.csv')

# Verificar os primeiros registros
print(df.head().to_string())

# Verificar os últimos registros
print(df.tail().to_string())

# Verificar qtd de linhas e colunas
print('Qtd: ', df.shape)

# Verificar tipos de dados (se é int, flot ou object)
print('Tipagem: \n', df.dtypes)

# Checar valores nulos
print('Valores nulos: \n', df.isnull().sum())