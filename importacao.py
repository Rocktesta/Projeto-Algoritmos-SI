import pandas as pd
import sqlite3
import pandas as pd

def importacao_db():
    
    conn = sqlite3.connect('Graph.db')

    # Escreva a consulta SQL que deseja executar
    query = 'SELECT * FROM grafo'

    # Carregue o resultado da consulta em um DataFrame
    df = pd.read_sql_query(query, conn)
    

    conn.close()

    df['origem'] = df['origem'].astype(str)
    df['destino'] = df['destino'].astype(str)
    graph_dict = {}

    # Percorre cada linha do DataFrame e preenche o dicionário
    for _, row in df.iterrows():
        origem, destino, peso = row['origem'], row['destino'], row['distancia']
        if origem not in graph_dict:
            graph_dict[origem] = {}
        graph_dict[origem][destino] = peso
    return graph_dict
importacao_db()

