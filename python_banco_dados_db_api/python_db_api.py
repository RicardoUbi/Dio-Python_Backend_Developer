import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Conexão com o banco de dados
conexao = sqlite3.connect("meu banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(conexao, cursor):
    cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(100))')
    conexao.commit()

def inserir_valores(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);', data)
    conexao.commit()

def atualizar_valores(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data)
    conexao.commit()

def excluir_valores(conexao, cursor, id):
    data = (id,) # Se não adicionar esta virgula após o id, pode ocorrer um erro.
    cursor.execute('DELETE FROM clientes WHERE id=?;', data)
    conexao.commit()

def inserir_muitos_valores(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?,?);', dados)
    conexao.commit()


def recuperar_registro(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?;", (id,))
    return cursor.fetchone()

def listar_registros(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome;")


#cliente = recuperar_registro(cursor, 2)
#print(dict(cliente))
#print(cliente["id"], cliente["nome"], cliente["email"])
#print(f'Seja bem vindo ao sistema {cliente["nome"]}')


#clientes = listar_registros(cursor)
#for cliente in clientes:
#    print(cliente)


#dados = [
#    ("Joao", "Joao@gmail.com"),
#    ("Jonas", "Jonas@gmail.com"),
#    ("Larissa", "Larissa@gmail.com"),
#    ("Ana", "Ana@gmail.com"),
#]

#inserir_muitos_valores(conexao, cursor, dados)
