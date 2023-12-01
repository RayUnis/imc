import sqlite3

def criar_tabela_pacientes():
    conn = sqlite3.connect('dados_pacientes.db')
    cursor = conn.cursor()

    # Criar a tabela "pacientes" se ela não existir
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

if __name__ == "__main__":
    criar_tabela_pacientes()
    print("Tabela 'pacientes' criada com sucesso.")
