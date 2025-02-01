from sklearn.cluster import KMeans

def agrupar_estados(df_final):
    """ Agrupa estados usando K-Means """
    kmeans = KMeans(n_clusters=3, random_state=42)
    df_final['Cluster'] = kmeans.fit_predict(df_final[['Razão']])
    
    return df_final