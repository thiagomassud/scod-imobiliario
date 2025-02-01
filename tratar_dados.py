import pandas as pd

def calcular_razao(df_empresas, df_populacao):
    """ Junta os dados de empresas e população para calcular a razão. """
    df_final = pd.merge(df_empresas, df_populacao, left_on=['Estado', 'Ano'], right_on=['UF', 'Ano'])
    df_final['Razão'] = df_final['População'] / df_final['Empresas_Ativas']
    
    return df_final