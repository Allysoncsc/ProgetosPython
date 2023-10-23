from main import connection, TABLE_NAME


with connection:
    with connection.cursor() as cursor:
        sql = f"SELECT * FROM {TABLE_NAME} "
        cursor.execute(sql)  # type: ignore
        data5 = cursor.fetchall()  # type: ignore
        for row in data5:
            _id, nome, idade = row
            print(_id, nome, idade)

    # # Lendo os valores com SELECT
    # with connection.cursor() as cursor:
    #     menor_id = int(input('Digite o menor id: '))
    #     maior_id = int(input('Digite o maior id: '))
    #     # menor_id = int(input('Digite o menor id: '))
    #     # maior_id = int(input('Digite o maior id: '))
    #     menor_id = 2
    #     maior_id = 4

    #     sql = (
    #         f'SELECT * FROM {TABLE_NAME} '
    #         'WHERE id BETWEEN %s AND %s  '
    #     )

    #     cursor.execute(sql, (menor_id, maior_id))  # type: ignore
    #     print(cursor.mogrify(sql, (menor_id, maior_id)))  # type: ignore
    #     # print(cursor.mogrify(sql, (menor_id, maior_id)))  # type: ignore
    #     data5 = cursor.fetchall()  # type: ignore

    #     for row in data5:
    #     # for row in data5:
    #     # print(row)

    # # Apagando com DELETE, WHERE e placeholders no PyMySQL
    # with connection.cursor() as cursor:
    #     sql = (
    #         f'DELETE FROM {TABLE_NAME} '
    #         'WHERE id = %s'
    #     )
    #     print(cursor.execute(sql, (1,)))  # type: ignore
    #     connection.commit()

    #     cursor.execute(f'SELECT * FROM {TABLE_NAME} ')  # type: ignore

    #     for row in cursor.fetchall():  # type: ignore
    #         print(row)
