import mysql.connector


class Database:
    ''' Database implementation for MySQL '''

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        
        self.connect()

    def connect(self):
        ''' Connect to MySQL '''
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def close(self):
        ''' Close connection to MySQL '''
        if self.connection:
            self.connection.close()

    def get_data(self, query):
        ''' Get data from MySQL '''
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result

    def insert_data(self, query, data):
        ''' Insert data into MySQL '''
        with self.connection.cursor() as cursor:
            cursor.execute(query, data)
            self.connection.commit()



class Forms:
    ''' Class used to create and gets forms '''

    def __init__(self, database):
        self.database = database

    def save(self, form):
        '''TODO: Save data to database'''
        return

    def get_forms(self):
        ''' Get all forms '''
        query = "SELECT * FROM form"
        return self.database.get_data(query)


# Ejemplo de uso
# db = Database('localhost', 'tu_usuario', 'tu_contraseña', 'tu_base_de_datos')
# db.connect()
# data = db.get_data('SELECT * FROM tabla')
# print(data)
# db.insert_data('INSERT INTO tabla (col1, col2) VALUES (%s, %s)',
#                ('valor1', 'valor2'))
# db.close()
