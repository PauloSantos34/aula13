import pandas as pd 

df = pd.read_excel('./aula_13/vendas_eletronicos.xlsx')
print(df.head(10))
print(df.head(20))
# Valor Máximo de faturamento total
print("\nMaior valor de faturamento total:")
print(df['Faturamento Total (R$)'].max())
# valor meno de faturamento

print("\nMenor valor de faturamento total:")
print(df['Faturamento Total (R$)'].min())
# Somatório das unidades vendidas

print("\nSomatório das unidades vendidas:")
print(df['Unidades Vendidas'].sum())

# Média dos preços por unidade
print("\nMédia dos preços dos produtos:")
print(df['Preço por Unidade (R$)'].mean())


