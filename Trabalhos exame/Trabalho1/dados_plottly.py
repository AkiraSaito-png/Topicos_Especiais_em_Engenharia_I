#Trabalhar com plotly e construir os gráficos:
#
#    - valor x mês por tipo, gráfico de linha.
#    - histograma numero funcionários x  cidades.
#    - histograma valor x cidades em cada tipo.
#
#   Diretório do documento:
#   https://docs.google.com/spreadsheets/d/1bQclG_lEMmKk54zatRpEbCyZTgAKlGZN9MhCkJkfx4Q/edit#gid=1581028379
#
#   Aluno: Akira Saito
#   Cód.: 831474
#
#%%
import plotly.express as px
import pandas as pd

dados = pd.read_excel('Trabalho1\dados\Dados_plotly (1).xlsx')

df = pd.DataFrame(dados)

# %%
#    - valor x mês por tipo, gráfico de linha.

dados_x = df['mês']
dados_y = df['Tipo']
fig = px.line(x = dados_x, y = dados_y)
fig.show()
# %%
#    - histograma numero funcionários x  cidades.

dados_x = df['cidade']
dados_y = df['n_funcionario']
fig = px.histogram(x= dados_x, y= dados_y)
fig.show()
# %%
#    - histograma valor x cidades em cada tipo.

dados_x = df[['valor']]
dados_y = df[['cidade']]
fig = px.histogram(x= dados_x, y= dados_y)
fig.show()