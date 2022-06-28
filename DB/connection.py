import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        """ Initializes a new connection to the database.

            return: None
        """
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
        """ Returns a list with the result of the query and the headers of the table.

        Args:
            query (string): The query to be executed.

        Returns:
            dict: A dictionary with the headers and the result of the query.
        """
        if self.connection.is_connected():
            try :
                cursor = self.connection.cursor()
                cursor.execute(query)
                return {'headers': [i[0] for i in cursor.description], 'query': cursor.fetchall()}
            except Error as ex:
                print("Error trying to get query: {0}".format(ex))
    
    def search(self, query):
        """ Returns the result of the query as a list of directories.

        Args:
            query (string): The query to be executed.

        Returns:
            list: List of directories with the result of the query.
        """
        if self.connection.is_connected():
            try :
                cursor = self.connection.cursor(dictionary=True)
                cursor.execute(query)
                return cursor.fetchall()
            except Error as ex:
                print("Error trying to search: {0}".format(ex))

    def add(self, query):
        """ Adds a new record to the database.

        Args:
            query (string): The query to be executed.

        Returns:
            int: The ID of the new record.
        """
        if self.connection.is_connected():
            try :
                cursor = self.connection.cursor()
                cursor.execute(query)
                last_id = cursor.lastrowid
                self.connection.commit()
                return last_id
            except Error as ex:
                print("Error trying to add: {0}".format(ex))
    
    def update(self, query):
        """ Updates a record in the database.

        Args:
            query (string): The query to be executed.

        Returns: None
        """
        if self.connection.is_connected():
            try :
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
                print("Updated successfully!")
            except Error as ex:
                self.connection.rollback()
                print("Error trying to update: {0}".format(ex))

    def delete(self, query):
        """ Deletes a record from the database.
        
            Args:
                query (string): The query to be executed.
                
            Returns: None
        """
        if self.connection.is_connected():
            try :
                cursor = self.connection.cursor()
                cursor.execute(query)
                self.connection.commit()
            except Error as ex:
                self.connection.rollback()
                print("Error trying to delete: {0}".format(ex))