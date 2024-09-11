import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('vendas.csv', delimiter=';', parse_dates=['DATA'])

dados['receita'] = dados['QUANTIDADE'] * dados['PRECO']
vendas_produto = dados.groupby('PRODUTO')['QUANTIDADE'].sum()

#Receita
plt.figure(figsize=(10, 5))
dados.groupby(dados['DATA'].dt.date)['receita'].sum().plot(kind='bar', color='skyblue')
plt.title('Receita Diária')
plt.xlabel('Data')
plt.ylabel('Receita (R$)')
plt.xticks(rotation=45)
plt.show()

#Por produto
plt.figure(figsize=(8, 5))
vendas_produto.plot(kind='bar', color='lightgreen')
plt.title('Quantidade Vendida por Produto')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=0)
plt.show()
