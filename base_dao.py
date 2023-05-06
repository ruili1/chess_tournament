import mysql.connector

class BaseDao:
    def get_connection(self):
        try:
            connection = mysql.connector.connect(user='root', password='eThan04292010a', host='127.0.0.1', database='chess_tournament')
            return connection
        except mysql.connector.Error as err:
            print(err)
