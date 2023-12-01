import sqlite3

conn = sqlite3.connect('dados_pacientes.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        endereco TEXT,
        peso REAL,
        altura REAL,
        imc REAL
    )
''')

conn.commit()
conn.close()