import sqlite3

def criar_tabelas():
    conn = sqlite3.connect('neral_agencia_virtual.db')
    cursor = conn.cursor()

    # Criar tabela de clientes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        endereco TEXT NOT NULL,
        identidade BLOB NOT NULL,
        comprovante_residencia BLOB NOT NULL,
        whatsapp TEXT NOT NULL
    )
    ''')

    # Criar tabela de profissionais
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS profissionais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        endereco TEXT NOT NULL,
        identidade BLOB NOT NULL,
        comprovante_residencia BLOB NOT NULL,
        whatsapp TEXT NOT NULL,
        servicos TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    criar_tabelas()
