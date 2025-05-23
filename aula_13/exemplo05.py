import pandas as pd

import numpy as np 


df = pd.read_excel('./aula_13/vendas_roupas.xlsx')
print(df.head(10))

# print(df.describe())

categoria = df['Categoria']
quantidade_vendida = df['Unidades Vendidas']
print(quantidade_vendida)
# print(quantidade_vendida)

media = np.mean(quantidade_vendida)
mediana = np.median(quantidade_vendida)

print("Média:", media)
print("Mediana:", mediana)

# organizar o DataFrame crescente por 'quantidade vendida'
quantidade_organizada = df.sort_values(by='Unidades Vendidas', ascending=True)

print(quantidade_vendida.values)

satisfacao = df[df['Satisfação'] == 'Baixo']


