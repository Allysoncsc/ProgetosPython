import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#criando tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
    'name TEXT, '
    'idade INTEGER'
    ')'
)

#inserindo valores
#assim está mais sujeito a SQL injection
cursor.execute(
    f'INSERT INTO {TABLE_NAME} ( name, idade) '
    'VALUES ("Allyson Correia",33),'
    '("goku",47),("vegeta",52),'
    '("goha",26),("kuririn",47)'
)
connection.commit()


#fechando conexão
cursor.close()
connection.close()
