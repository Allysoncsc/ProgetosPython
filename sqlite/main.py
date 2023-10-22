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

if __name__ == '__main__':

    #deleta a tabela e resetando sequencia
    # cursor.execute(
    #     f'DELETE FROM {TABLE_NAME}'
    # )
    # cursor.execute(
    #     f'DELETE FROM sqlite_sequence WHERE name={TABLE_NAME}'
    # )


    #inserindo valores
    #assim está mais sujeito a SQL injection
    # cursor.execute(
    #     f'INSERT INTO {TABLE_NAME} ( name, idade) '
    #     'VALUES ("Allyson Correia",33),'
    #     '("goku",47),("vegeta",52),'
    #     '("goha",26),("kuririn",47)'
    # )
    sql = (
        f'INSERT INTO {TABLE_NAME} ( name, idade) '
        'VALUES '
        '(?,?)'    
    )
    #cursor.execute(sql,['Hiei',232])
    cursor.executemany(sql,[['yusuke',17],['kurama',256],['kuwabara',17]])
    connection.commit()


    #fechando conexão
    cursor.close()
    connection.close()
