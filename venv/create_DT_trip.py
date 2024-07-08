from mysql.connector import Error
from conection_cursor_DB import connection


# Создание таблиц. Вставка записей.

# Создадим новый вариант функции execute_query():
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()             # сохранение данных в таблице на сервере
        print("Query executed successfully")
    except Error as e:
        print(f"The error {e}")


def printing_data(connection, selection):
    cursor = connection.cursor()
    try:
        cursor.execute(selection)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"The error {e}")


    # Создаем таблицу trip
create_table_trip = """
CREATE TABLE IF NOT EXISTS trip (
    trip_id    INT PRIMARY KEY AUTO_INCREMENT,
    name       VARCHAR(30),
    city       VARCHAR(25),
    per_diem   DECIMAL(8, 2),
    date_first DATE,
    date_last  DATE
) ENGINE = InnoDB
"""
execute_query(connection, create_table_trip)

    # Заполним таблицу trip
insert_values_to_trip = """
INSERT INTO trip (trip_id, name, city, per_diem, date_first, date_last)
VALUES 
    ('1', 'Баранов П.Е.', 'Москва', '700', '2020-01-12', '2020-01-17'),
	('2', 'Абрамова К.А.', 'Владивосток', '450', '2020-01-14', '2020-01-27'),
	('3', 'Семенов И.В.', 'Москва', '700', '2020-01-23', '2020-01-31'),
	('4', 'Ильиных Г.Р.', 'Владивосток', '450', '2020-01-12', '2020-02-02'),
	('5', 'Колесов С.П.', 'Москва', '700', '2020-02-01', '2020-02-06'),
	('6', 'Баранов П.Е.', 'Москва', '700', '2020-02-14', '2020-02-22'),
	('7', 'Абрамова К.А.', 'Москва', '700', '2020-02-23', '2020-03-01'),
	('8', 'Лебедев Т.К.', 'Москва', '700', '2020-03-03', '2020-03-06'),
	('9', 'Колесов С.П.', 'Новосибирск', '450', '2020-02-27', '2020-03-12'),
	('10', 'Семенов И.В.', 'Санкт-Петербург', '700', '2020-03-29', '2020-04-05'),
	('11', 'Абрамова К.А.', 'Москва', '700', '2020-04-06', '2020-04-14'),
	('12', 'Баранов П.Е.', 'Новосибирск', '450', '2020-04-18', '2020-05-04'),
	('13', 'Лебедев Т.К.', 'Томск', "450", '2020-05-20', '2020-05-31'),
	('14', 'Семенов И.В.', 'Санкт-Петербург', '700', '2020-06-01', '2020-06-03'),
	('15', 'Абрамова К.А.', 'Санкт-Петербург', '700', '2020-05-28', '2020-06-04'),
	('16', 'Федорова А.Ю.', 'Новосибирск', '450', '2020-05-25', '2020-06-04'),
	('17', "Колесов С.П.", 'Новосибирск', '450', '2020-06-03', '2020-06-12'),
	('18', 'Федорова А.Ю.', 'Томск', '450', '2020-06-20', '2020-06-26'),
	('19', 'Абрамова К.А.', 'Владивосток', '450', '2020-07-02', '2020-07-13'),
	('20', 'Баранов П.Е.', 'Воронеж', '450', '2020-07-19', '2020-07-25');
"""
execute_query(connection, insert_values_to_trip)
    # Выведем в консоль таблицу trip
print('\nТаблица trip')
printing_data(connection, 'select * from trip')