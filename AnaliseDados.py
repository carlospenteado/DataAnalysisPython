# Passo 1: Importar a base de dados - Passo

import pandas as pd
tabela = pd.read_csv("C:/Users/Usuario/PycharmProjects/AnaliseDadosComPython/BaseDados/ClientesBanco.csv", encoding="latin1")

# 2: Visualizar e tratar essa base de dados
tabela = tabela.drop("CLIENTNUM", axis=1)

# Passo 3: "Verificar, dar uma olhada" na sua base de dados
qtde_categoria = tabela["Categoria"].value_counts()
print(qtde_categoria)

qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True)
print(qtde_categoria_perc)


# Passo 4: Construir uma análise para identificar o motivo de cancelamento

# Objetivo Identificar qual o motivo ou os principais motivos dos clientes estarem cancelando o cartão de crédito.

import plotly.express as px

for coluna in tabela:
  grafico = px.histogram(tabela, x=coluna, color="Categoria")
  grafico.show()







