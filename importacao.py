import pandas as pd
import sqlite3
# linha "import pandas as pd" script que transforma o banco de dados com livraria pandas (já tinha)

def importacao_db():
    #conecta-se ao banco de dados
    conn = sqlite3.connect('Graph.db')

    # Escreva a consulta SQL que deseja executar
    query = 'SELECT * FROM grafo'

    # Carregue o resultado da consulta em um DataFrame
    df = pd.read_sql_query(query, conn)
    

    conn.close()
    #termina a conexão 
    df['origem'] = df['origem'].astype(str)
    df['destino'] = df['destino'].astype(str)
    graph_dict = {} # o grafo é um dicionário de dicionários

    # Percorre cada linha do DataFrame e preenche o dicionário
    for _, row in df.iterrows():
        origem, destino, peso = row['origem'], row['destino'], row['distancia']
        if origem not in graph_dict:
            graph_dict[origem] = {}
        graph_dict[origem][destino] = peso
    return graph_dict #retorna o grafo completo
importacao_db()

