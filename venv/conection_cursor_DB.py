import mysql.connector
from mysql.connector import Error
from config import host, user, password, db_name

# Подключение к MySQL, создание объектов connection / cursor, создание БД (bd_name)

    # Установим подключение к серверу MySQL. Функция подключается к серверу MySQL и возвращает объект подключения:
def create_connection(host, user, password):
	connection = None
	try:
		connection = mysql.connector.connect(
		    host=host,
		    user=user,
		    passwd=password
		        )
		print("Connection to MySQL server successful")
	except Error as e:
		print(f"The error {e} occurred")
	return connection
connection = create_connection(host, user, password)

	# Создадим базу данных, передав в функцию Объект connection и query – строковый запрос о создании базы данных.

def create_database(connection, query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)					# Для выполнения запросов используется объект cursor.
		print("Database created successfully")
	except Error as e:
		print(f"The error {e}")

	# Создадим базу данных db_name на сервере MySQL:
create_db_query = "create database MySQL_Metelica_practicum"
create_database(connection, create_db_query)

	# объект connection, возвращаемый функцией create_connection() подключен к серверу MySQL. Чтобы подключиться к базе
	# данных, нужно изменить create_connection() следующим образом:
def create_connection(host, user, password, db_name):
	connection = None
	try:
		connection = mysql.connector.connect(
			host=host,
			user=user,
			passwd=password,
			database=db_name
				)
		print("Connection to MySQL DB successful")
	except Error as e:
		print(f"The error {e}")
	return connection

connection = create_connection(host, user, password, db_name)

