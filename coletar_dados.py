import requests
import pandas as pd

def coletar_dados_empresas():
    """
    Faz uma requisição HTTP para a API do SIDRA/IBGE e coleta os dados de número de empresas ativas por estado.
    
    Retorna:
        pd.DataFrame: DataFrame contendo os dados com as colunas ['Estado', 'Ano', 'Empresas_Ativas'].
    """
    # URL corrigida (sem faixa específica)
    url = "https://apisidra.ibge.gov.br/values/t/1757/n3/all/p/2007-2020/d/0"

    response = requests.get(url)

    if response.status_code != 200:
        print("Resposta da API:", response.text)  # Exibir resposta detalhada
        raise Exception(f"Erro ao buscar dados: {response.status_code}")
    
    data = response.json()  # Converte JSON para dicionário

    # Verificar os primeiros registros retornados
    print("Exemplo de dado retornado:", data[:5])

    # Remover a primeira linha que contém cabeçalhos
    data = data[1:]

    # Criar DataFrame
    df = pd.DataFrame(data)

    # Exibir as colunas disponíveis para checar os nomes
    print("Colunas disponíveis:", df.columns)

    # Selecionar apenas as colunas relevantes
    df = df[['D1N', 'D3N', 'V']]
    df.columns = ['Estado', 'Ano', 'Empresas_Ativas']

    # Remover valores inválidos ("-")
    df = df[df['Empresas_Ativas'] != '-']

    # Converter colunas para tipos numéricos
    df['Ano'] = df['Ano'].astype(int)
    df['Empresas_Ativas'] = df['Empresas_Ativas'].astype(int)

    return df

# Testar a função
df_empresas = coletar_dados_empresas()
print(df_empresas.head())  # Exibir os primeiros registros

