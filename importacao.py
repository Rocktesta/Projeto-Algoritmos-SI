import pandas as pd

import sqlite3
import pandas as pd


conn = sqlite3.connect('Graph.db')

# Escreva a consulta SQL que deseja executar
query = 'SELECT * FROM grafo'

# Carregue o resultado da consulta em um DataFrame
df = pd.read_sql_query(query, conn)
print(df)

conn.close()
