import sqlite3

registro = 'senha.db'

script_registro = """CREATE TABLE IF NOT EXISTS Registro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                senha INTEGER NOT NULL
            );"""


try:
    with sqlite3.connect(registro) as conn:
        cur = conn.cursor()
        cur.execute(script_registro)
        conn.commit()
        print("Tabelas Criadas com Sucesso")
except sqlite3.OperationalError as e:
    print("ERRO: ", e)

email = input('Digite seu email: ')
senha = input('Digite sua senha: ')

sql = "INSERT INTO login (email, senha) VALUES (?,?)"

try:
    with sqlite3.connect(registro) as conn:
         cur = conn.cursor()
         cur.execute(sql, (email, senha))
         conn.commit()
except sqlite3.OperationalError as e:
    print("ERRO: ", e)

sql = "SELECT * FROM Alunos"

try:
    with sqlite3.connect(registro) as conn:
         cur = conn.cursor()
         cur.execute(sql)
         res = cur.fetchall()
         print(res)
except sqlite3.OperationalError as e:
    print("ERRO: ", e)