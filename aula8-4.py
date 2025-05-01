"""
O que são Outliers?
Outliers (valores atípicos) são observações que se desviam significativamente da maioria dos dados em um conjunto. Eles podem:
- Ser erros (ex.: digitação de idade como 150 anos).
- Representar eventos raros mas válidos (ex.: um cliente que gasta 10x mais que a média).

Impacto:
- Distorcem estatísticas (média, desvio padrão).
- Afetam modelos de machine learning e análises.

Métodos de Identificação de Outliers
1) Filtro Básico (Domínio do Conhecimento)
Como funciona: Remove valores fora de um intervalo plausível definido por regras de negócio.
    Ex.: Idades humanas fora de [0, 120].

2) IQR (Intervalo Interquartil)
Como funciona:
    Calcula a diferença entre o 3º quartil (Q3) e o 1º quartil (Q1): IQR = Q3 - Q1.
Limites:
    Inferior: Q1 - 1.5 * IQR.
    Superior: Q3 + 1.5 * IQR.
Valores fora desses limites são outliers.

3) Z-Score (Desvio Padrão)
Como funciona:
    Calcula quantos desvios padrão (σ) um valor está da média (μ).
    Fórmula: Z = (x - μ) / σ.
    Limiar comum: |Z| > 3 (valores além de 3σ são considerados outliers).
"""

# Dataset de Exemplo
import pandas as pd
import numpy as np

# Criar DataFrame com outliers
data = {'idade': [25, 30, 35, 40, 150, 28, 32, -10, 45, 200]}
df = pd.DataFrame(data)
print('original: \n', df)

# 1) Filtro Básico:
df_clean_fb = df[(df['idade'] >= 0) & (df['idade'] <= 120)]
print('Filtro Básico: \n', df_clean_fb)

print(df['idade'].describe())
print(df_clean_fb['idade'].describe())

# 2) IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

df_clean_iqr = df[(df['idade'] >= limite_inferior) & (df['idade'] <= limite_superior)]
print('IQR: \n', df_clean_iqr)

print(df['idade'].describe())
print(df_clean_iqr['idade'].describe())

# 3) Z-Score
from scipy.stats import zscore

df['zscore'] = zscore(df['idade'])
df_clean_zs = df[abs(df['zscore']) <= 3]
print('Z-Score: \n', df_clean_zs)

print(df['idade'].describe())
print(df_clean_zs['idade'].describe())