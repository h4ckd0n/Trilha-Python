import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "my_bank.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("INSET INTO clientes (nome, email)VALUES (?,?)", ()"Test 3", "teste2@gmail.com"))
    cliente = cursor.fetchone("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2 "Teste 3", "teste3@gmail.com"))
    conexao.commit()
except Exception as exc:
    print(f"Ops! um erro ocorreu! {exc}")
    conexao.rollback()