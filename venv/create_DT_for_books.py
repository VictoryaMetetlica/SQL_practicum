from mysql.connector import Error
from conection_cursor_DB import connection
from create_DT_trip import execute_query, printing_data

# В интернет-магазине продаются книги. Каждая книга имеет название, написана одним автором,относится к одному жанру,
# имеет определенную цену. В магазине в наличии есть несколько экземпляров каждой книги. Покупатель регистрируется
# на сайте интернет-магазина, задает свое имя и фамилию, электронную почту и город проживания. Он может сформировать
# один или несколько заказов, для каждого заказа написать какие-то пожелания. Каждый заказ включает одну или несколько
# книг, каждую книгу можно заказать в нескольких экземплярах. Затем заказ проходит ряд последовательных этапов
# (операций): оплачивается, упаковывается, передается курьеру или транспортной компании для транспортировки и, наконец,
# доставляется покупателю. Фиксируется дата каждой операции. Для каждого города известно среднее время доставки книг.
# При этом в магазине ведется учет книг, при покупке их количество уменьшается, при поступлении товара увеличивается,
# при исчерпании количества – оформляется заказ и пр.

    # Создаем таблицу author
create_table_author = """
CREATE TABLE IF NOT EXISTS author (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    name_author VARCHAR(50)	
                                   ) ; 
                        """
execute_query(connection, create_table_author)

    # Заполним таблицу author
insert_values_to_author = """
INSERT INTO author (name_author)
VALUES ('Булгаков М.А.'),('Достоевский Ф.М.'), ('Есенин С.А.'), ('Пастернак Б.Л.'),  ('Лермонтов М.Ю.');
       """
execute_query(connection, insert_values_to_author)
print('\nТаблица author:')
printing_data(connection, 'select DISTINCT name_author from author')

    # Создаем таблицу genre
create_table_genre = """
CREATE TABLE IF NOT EXISTS genre (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    name_genre VARCHAR(30) 	
        ) ENGINE = InnoDB
        """
execute_query(connection, create_table_genre)

insert_values_to_genre = """
    INSERT INTO genre(name_genre)
    VALUES ('Роман'), ('Поэзия'), ('Приключения');
"""
execute_query(connection, insert_values_to_genre)
print('\nТаблица genre:')
printing_data(connection, 'select DISTINCT name_genre from genre')

    # Создаем таблицу book
create_table_book = """
CREATE TABLE IF NOT EXISTS book (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    author_id INT NOT NULL,
    genre_id INT,
    price DECIMAL(8, 2),
    amount INT,
    FOREIGN KEY (author_id) REFERENCES author (author_id)  ON DELETE CASCADE,
    FOREIGN KEY (genre_id)  REFERENCES genre (genre_id)    ON DELETE SET NULL 	
    ) ENGINE = InnoDB
"""
execute_query(connection, create_table_book)

insert_values_to_book = """
INSERT INTO book (title, author_id, genre_id, price, amount)
VALUES  ('Мастер и Маргарита', 1, 1, 670.99, 3), ('Белая гвардия ', 1, 1, 540.50, 5), ('Идиот', 2, 1, 460.00, 10),
        ('Братья Карамазовы', 2, 1, 799.01, 2), ('Игрок', 2, 1, 480.50, 10), ('Стихотворения и поэмы', 3, 2, 650.00, 15),
        ('Черный человек', 3, 2, 570.20, 6), ('Лирика', 4, 2, 518.99, 2); 
"""
execute_query(connection, insert_values_to_book)
print('\nТаблица book:')
printing_data(connection, 'select DISTINCT title, author_id, genre_id, price, amount from book')

    # Создаем таблицу city
create_table_city = """
CREATE TABLE IF NOT EXISTS city (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    name_city VARCHAR(30),
    days_delivery INT	
    ) ENGINE = InnoDB
    """
execute_query(connection, create_table_city)

insert_values_to_city = """
    INSERT INTO city(name_city, days_delivery)
    VALUES ('Москва', 5),  ('Санкт-Петербург', 3),   ('Владивосток', 12);
"""
execute_query(connection, insert_values_to_city)
print('\nТаблица city:')
printing_data(connection, 'select DISTINCT name_city, days_delivery from city')

    # Создаем таблицу client
create_table_client = """
CREATE TABLE IF NOT EXISTS client (
    client_id INT PRIMARY KEY AUTO_INCREMENT,
    name_client VARCHAR(50),
    city_id INT,
    email VARCHAR(30),
    FOREIGN KEY (city_id) REFERENCES city (city_id)	) ENGINE = InnoDB
    """
execute_query(connection, create_table_client)

insert_values_to_client = """
    INSERT INTO client(name_client, city_id, email)
    VALUES ('Баранов Павел', 3, 'baranov@test'), ('Абрамова Катя', 1, 'abramova@test'), 
    ('Семенонов Иван', 2, 'semenov@test'), ('Яковлева Галина', 1, 'yakovleva@test');
"""
execute_query(connection, insert_values_to_client)
print('\nТаблица client')
printing_data(connection, 'select DISTINCT name_client, city_id, email from client')

    # Создаем таблицу buy
create_table_buy = """
CREATE TABLE IF NOT EXISTS buy(
    buy_id INT PRIMARY KEY AUTO_INCREMENT,
    buy_description VARCHAR(100),
    client_id INT,
    FOREIGN KEY (client_id) REFERENCES client (client_id) 	) ENGINE = InnoDB
"""
execute_query(connection, create_table_buy)

insert_values_to_buy = """
    INSERT INTO buy (buy_description, client_id)
    VALUES ('Доставка только вечером', 1), (NULL, 3), ('Упаковать каждую книгу по отдельности', 2), (NULL, 1); 
"""
execute_query(connection, insert_values_to_buy)
print('\nТаблица buy')
printing_data(connection, 'select DISTINCT buy_description, client_id from buy')

    # Создаем таблицу buy_book
create_table_buy_book = """
CREATE TABLE IF NOT EXISTS buy_book(
    buy_book_id INT PRIMARY KEY AUTO_INCREMENT,
    buy_id INT,
    book_id INT,
    amount INT,
    FOREIGN KEY (buy_id) REFERENCES buy (buy_id),
    FOREIGN KEY (book_id) REFERENCES book (book_id) 	) ENGINE = InnoDB
    """
execute_query(connection, create_table_buy_book)

insert_values_to_buy_book = """
    INSERT INTO buy_book(buy_id, book_id, amount)
    VALUES (1, 1, 1), (1, 7, 2), (1, 3, 1), (2, 8, 2), (3, 3, 2), (3, 2, 1), (3, 1, 1), (4, 5, 1);
    """
execute_query(connection, insert_values_to_buy_book)
print('\n Таблица buy_book:')
printing_data(connection, 'select DISTINCT buy_id, book_id, amount from buy_book')

    # Создаем таблицу step
create_table_step = """
CREATE TABLE IF NOT EXISTS step (
    step_id INT PRIMARY KEY AUTO_INCREMENT,
    name_step VARCHAR(30)	) ENGINE = InnoDB
    """
execute_query(connection, create_table_step)

insert_values_to_step = """
    INSERT INTO step(name_step)
    VALUES ('Оплата'),  ('Упаковка'), ('Транспортировка'), ('Доставка');
"""
execute_query(connection, insert_values_to_step)
print('\n Таблица step')
printing_data(connection, 'select DISTINCT name_step from step')

    # Создаем таблицу buy_step
create_table_buy_step = """
CREATE TABLE IF NOT EXISTS buy_step (
    buy_step_id INT PRIMARY KEY AUTO_INCREMENT,
    buy_id INT,
    step_id INT,
    date_step_beg DATE,
    date_step_end DATE,
    FOREIGN KEY (buy_id) REFERENCES buy (buy_id),
    FOREIGN KEY (step_id) REFERENCES step (step_id)	) ENGINE = InnoDB
    """
execute_query(connection, create_table_buy_step)

insert_values_to_buy_step = """
    INSERT INTO buy_step(buy_id, step_id, date_step_beg, date_step_end)
    VALUES (1, 1, '2020-02-20', '2020-02-20'), (1, 2, '2020-02-20', '2020-02-21'),  (1, 3, '2020-02-22', '2020-03-07'),
   (1, 4, '2020-03-08', '2020-03-08'),  (2, 1, '2020-02-28', '2020-02-28'),  (2, 2, '2020-02-29', '2020-03-01'),
   (2, 3, '2020-03-02', NULL), (2, 4, NULL, NULL), (3, 1, '2020-03-05', '2020-03-05'), (3, 2, '2020-03-05', '2020-03-06'),
   (3, 3, '2020-03-06', '2020-03-10'),  (3, 4, '2020-03-11', NULL), (4, 1, '2020-03-20', NULL), (4, 2, NULL, NULL),
    (4, 3, NULL, NULL), (4, 4, NULL, NULL);
    """
execute_query(connection, insert_values_to_buy_step)
print('\n Таблица buy_step')
printing_data(connection, 'select DISTINCT buy_id, step_id, date_step_beg, date_step_end from buy_step')
