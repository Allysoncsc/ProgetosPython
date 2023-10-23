import pymysql


TABLE_NAME = "clientes"


connection = pymysql.connect(
    host="localhost", user="root", password="0204aw", database="base_de_dados"
)
# cursor = connection.cursor()

# cursor.close()
# connection.close()
# já fecha automaticaaaamente

if __name__ == "__main__":
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( "
                "id INT NOT NULL AUTO_INCREMENT, "
                "nome varchar(50) NOT NULL, "
                "idade INT NOT NULL, "
                "PRIMARY KEY (id)"
                ") "
            )

            sqlinsert = (
                f"INSERT INTO {TABLE_NAME} "
                "(nome,idade) "
                "VALUES "
                "(%s,%s)"
                # '("Allyson Correia",33),'
                # '("goku",47),("vegeta",52),'
                # '("goha",26),("kuririn",47),("Hiei",232)'
            )

            cursor.execute(sqlinsert, ("yusuke", 17))

        connection.commit()

        # importando de um dicionario
        # with connection.cursor() as cursor:
        #     sql = (
        #         f'INSERT INTO {TABLE_NAME} '
        #         '(nome, idade) ' #nome da tabela mysql
        #         'VALUES '
        #         '(%(name)s, %(age)s) ' #nome no dicionario
        #     )
        #     data2 = {
        #         "age": 37,
        #         "name": "Le",
        #     }
        #     result = cursor.execute(sql, data2)  # type: ignore
        #     print(sql)
        #     print(data2)
        #     print(result)
        # connection.commit()

        # with connection.cursor() as cursor:
        #     sql = (
        #         f'INSERT INTO {TABLE_NAME} '
        #         '(nome, idade) '
        #         'VALUES '
        #         '(%(name)s, %(age)s) '
        #     )
        #     data3 = (
        #         {"name": "Sah", "age": 33, },
        #         {"name": "Júlia", "age": 74, },
        #         {"name": "Rose", "age": 53, },
        #     )
        #     result = cursor.executemany(sql, data3)  # type: ignore
        #     # print(sql)
        #     # print(data3)
        #     # print(result)
        # connection.commit()

        # with connection.cursor() as cursor:
        #     sql = (
        #         f'INSERT INTO {TABLE_NAME} '
        #         '(nome, idade) '
        #         'VALUES '
        #         '(%s, %s) '
        #     )
        #     data4 = (
        #         ("Siri", 22, ),
        #         ("Helena", 15, ),
        #     )
        #     result = cursor.executemany(sql, data4)  # type: ignore
        #     print(sql)
        #     print(data2)
        #     print(data4)
        #     print(result)
        # connection.commit()
