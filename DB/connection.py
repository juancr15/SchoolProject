import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='school'
            )
        except Error as ex:
            print("Error trying to connect to DB: {0}".format(ex))