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
    
    def get_list(self, query):
        if self.connection.is_connected():
            try :
                cursor = self.connection.cursor()
                cursor.execute(query)
                return {'headers': [i[0] for i in cursor.description], 'query': cursor.fetchall()}
            except Error as ex:
                print("Error trying to get query: {0}".format(ex))

    def add(self, query):
        if self.connection.is_connected():
            try :
                cursor = self.connection.cursor()
                cursor.execute(query)
                last_id = cursor.lastrowid
                self.connection.commit()
                return last_id
            except Error as ex:
                print("Error trying to add: {0}".format(ex))