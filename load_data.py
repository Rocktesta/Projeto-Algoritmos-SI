import sqlite3
from scipy.io import mmread

# path relativo
mtx_file_path = 'projeto_algoritmos\\USAir97\\USAir97.mtx'

matrix = mmread(mtx_file_path)

dense_matrix = matrix.toarray() if hasattr(matrix, 'toarray') else matrix

conn = sqlite3.connect('Graph.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS grafo (
        origem INTEGER,
        destino INTEGER,
        distancia REAL
    )
''')

rows, cols = dense_matrix.shape
for i in range(rows):
    for j in range(cols):
        value = dense_matrix[i, j]
        if value != 0:  
            cur.execute('INSERT INTO grafo (origem, destino, distancia) VALUES (?, ?, ?)', (i, j, value))

conn.commit()
conn.close()
