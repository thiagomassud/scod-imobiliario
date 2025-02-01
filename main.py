from coletar_dados import coletar_dados_empresas
from tratar_dados import calcular_razao
from previsao import prever_razao
from clusterizacao import agrupar_estados
from visualizar import plotar_razao
import pandas as pd

# 1️⃣ Coletar dados
df_empresas = coletar_dados_empresas()

# (Aqui você também deve carregar o arquivo populacional do IBGE)
df_populacao = pd.read_csv("populacao_processada.csv")

# 2️⃣ Calcular a razão População/Empresas
df_final = calcular_razao(df_empresas, df_populacao)

# 3️⃣ Prever 2021 e 2022
df_previsoes = prever_razao(df_final)

# 4️⃣ Adicionar previsões aos dados finais
df_final = pd.concat([df_final, df_previsoes])

# 5️⃣ Agrupar estados
df_final = agrupar_estados(df_final)

# 6️⃣ Plotar gráficos
plotar_razao(df_final)

# 7️⃣ Salvar o resultado final
df_final.to_csv("resultado_final.csv", index=False)