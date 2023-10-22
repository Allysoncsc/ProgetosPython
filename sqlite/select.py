import sqlite3
from pathlib import Path
from main import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id in (9,10,11)')
# connection.commit()

cursor.execute(f'UPDATE {TABLE_NAME} SET idade = 251 WHERE id = 7')
connection.commit()


cursor.execute(f'SELECT * FROM {TABLE_NAME}')
somaidade = 0
contador = 0
for row in cursor.fetchall():
    _id, name, age = row
    contador += 1
    somaidade += int(age)
    print(f'{_id} - {name} - {age}')

print(f'\n {somaidade / contador:.2f}')

#fechando conexão
cursor.close()
connection.close()
