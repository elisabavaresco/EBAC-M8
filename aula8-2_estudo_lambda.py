import pandas as pd

# Função para calcular o cubo de um número
def eleva_cubo(x):
    return x ** 3

# A expressão lambda é uma form ade escrever uma função em uma linha
# Expressão de lambda para calcular o cubo de um número:
eleva_cubo_lambda = lambda x: x ** 3

print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

df = pd.DataFrame({'numeros': [1, 2, 3, 4, 5, 10]})

# aplicando funções e criando colunas
df['cubo_funcao'] = df['numeros'].apply(eleva_cubo)
df['cubo_lambda'] = df['numeros'].apply(lambda x: x ** 3)
print(df)