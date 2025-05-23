import numpy as np

valor = np.array([150, 180, 200, 220, 250, 280, 300, 320, 400, 1500])
# calculando a média
media = np.mean(valor)
print('Média: ', media)

# calculando a mediana

mediana = np.median(valor)
print('Mediana: ', mediana)

print('A Mediana representa o valor típico das vendas: ', mediana)

q1 = np.quantile(valor, 0.25)
q2 = np.quantile(valor, 0.50)
q3 = np.quantile(valor, 0.75)

print('Q1: ', q1)
print('Q2: ', q2)
print('Q3: ', q3)

media = np.mean(valor)
print('Média: ', media)

# calculando a mediana

mediana = np.median(valor)
print('Mediana: ', mediana)