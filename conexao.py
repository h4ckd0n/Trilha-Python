import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "my_bank.sqlite")
cursor = conexao.cursor()

def criar_tabela(conexao, cursor):
    cursor.execute("CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
)
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes(nome, email) VALUES (?,?);", data )
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)    
    conexao.commit()

atualizar_registro(conexao, cursor, "Thiago Silva", "joni@outlook.com", 2)

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes(nome, email) VALUES (?,?);", dados)
    conexao.commit()

dados = [
    ("João", "john@gmail.com"),
    ("Maria", "mart@outlook.com"),
    ("José", "jos@gmail.com"),

]
inserir_muitos(conexao, cursor, dados)

def recuperar_cliente(cursor):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")

cliente = recuperar_cliente(cursor, 2)
print(cliente)

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)