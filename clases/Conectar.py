import mysql.connector


class Conectar:
    def __init__(self) -> None:
        self.__bd = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Zeus2801',
            database='test'
        )

        self.__cursor = self.__bd.cursor()

    def ejecutar(self, sql):
        try:
            self.__cursor.execute(sql)
            self.__bd.commit()

            return self.__cursor.rowcount

        except mysql.connector.Error as e:
            return 'Error: '+str(e)