from create_DT_for_books import connection, execute_query, printing_data


print('\n Вывести все заказы Баранова Павла (какие книги, по какой цене и в каком количестве он заказал) в отсортированном \
по номеру заказа и названиям книг виде')

request_for_Baranov = """
SELECT DISTINCT buy.buy_id, book.title, book.price, buy_book.amount
FROM buy
     JOIN client USING (client_id)
     JOIN buy_book USING (buy_id)
     JOIN book USING (book_id)
WHERE client.name_client = 'Баранов Павел'
ORDER BY buy.buy_id, book.title;
"""
printing_data(connection, request_for_Baranov)

print('\n Посчитать, сколько раз была заказана каждая книга, для книги вывести ее автора (нужно посчитать, в каком \
количестве заказов фигурирует каждая книга). Результат отсортировать сначала по фамилиям авторов, а потом по названиям \
книг. Последний столбец назвать Количество.')

count_for_each_book = """
select DISTINCT name_author, title, 
    IF(COUNT(buy_book.amount) IS NULL, 0, COUNT(buy_book.amount)) AS Количество
from author 
    join book on author.author_id = book.author_id
    left join buy_book on book.book_id = buy_book.book_id
group by name_author, title
order by name_author, title
"""
printing_data(connection, count_for_each_book)

print('\n Вывести города, в которых живут клиенты, оформлявшие заказы в интернет-магазине. Указать количество заказов в \
каждый город, этот столбец назвать Количество. Информацию вывести по убыванию количества заказов, а затем в \
алфавитном порядке по названию городов.')

clients_cities = """
select DISTINCT name_city, count(buy.client_id) as Количество
from city
    join client using (city_id)
    join buy using (client_id)
group by name_city
order by Количество desc, name_city
"""
printing_data(connection, clients_cities)

print('\n Вывести номера всех оплаченных заказов и даты, когда они были оплачены.')
ended_orders = """
select DISTINCT buy_id, date_step_end
from buy_step
where step_id = 1 and date_step_end is not null
"""
printing_data(connection, ended_orders)

print('\n Вывести информацию о каждом заказе: его номер, кто его сформировал (фамилия пользователя) и его стоимость (сумма '
      'произведений количества заказанных книг и их цены), в отсортированном по номеру заказа виде. Последний столбец '
      'назвать Стоимость.')

each_order_info = """
select DISTINCT buy_id, name_client, sum(price * buy_book.amount) as Стоимость 
from buy_book
    join buy using(buy_id)
    join client using(client_id)
    join book using(book_id)
group by buy_id
order by buy_id
"""
printing_data(connection, each_order_info)

print('\n Вывести номера заказов (buy_id) и названия этапов, на которых они в данный момент находятся. Если заказ доставлен '
      '– информацию о нем не выводить. Информацию отсортировать по возрастанию buy_id. Текущим считается тот этап, для '
      'которого заполнена дата начала этапа и не заполнена дата его окончания.')
current_steps_situation = """
select DISTINCT buy_id, name_step
from buy_step
    join step using(step_id)
where date_step_beg is not null and date_step_end is null 
order by buy_id
"""
printing_data(connection, current_steps_situation)

print('\n В таблице city для каждого города указано количество дней, за которые заказ может быть доставлен в этот город '
      '(рассматривается только этап Транспортировка). Для тех заказов, которые прошли этап транспортировки, вывести '
      'количество дней за которое заказ реально доставлен в город. А также, если заказ доставлен с опозданием, указать '
      'количество дней задержки, в противном случае вывести 0. В результат включить номер заказа (buy_id), а также '
      'вычисляемые столбцы Количество_дней и Опоздание. Информацию вывести в отсортированном по номеру заказа виде. Для '
      'вычисления поля «Опоздание» используйте функцию if(), а для вычисления разности дат – функцию DATEDIFF(). '
      'Если доставка еще не осуществлена, то поле date_step_end для этапа Транспортировка- пусто. ')

transportations = """
select DISTINCT
    buy_id, 
    DATEDIFF(date_step_end, date_step_beg) AS 'Количество_дней',
    IF(DATEDIFF(date_step_end, date_step_beg) > days_delivery, DATEDIFF(date_step_end, date_step_beg) - days_delivery, 0) AS 'Опоздание'
from buy_step
    join buy    using(buy_id)
    join client using(client_id)
    join city    using(city_id)
where step_id = 3 and DATEDIFF(date_step_end, date_step_beg) is not null
order by buy_id
"""
printing_data(connection, transportations)

print('\n Выбрать всех клиентов, которые заказывали книги Достоевского, информацию вывести в отсортированном по алфавиту '
      'виде. В решении используйте фамилию автора, а не его id.')
dostoevsky_clients = """
select distinct name_client
from client
    join buy      using(client_id)
    join buy_book using(buy_id)
    join book     using(book_id)
    join author   using(author_id)
where name_author = 'Достоевский Ф.М.'
order by name_client
"""
printing_data(connection, dostoevsky_clients)

print('\n Вывести жанр (или жанры), в котором было заказано больше всего экземпляров книг, указать это количество. '
      'Последний столбец назвать Количество.')
favorite_genre = """
select distinct name_genre, sum(buy_book.amount) as Количество
from genre
    join book using(genre_id)
    join buy_book using(book_id)
group by name_genre
having sum(buy_book.amount) = 
    (
    select max(sum_amount)
    from 
        (select sum(buy_book.amount) AS sum_amount 
         from buy_book
             join book using(book_id)
         group by genre_id) query_in
        );
"""
printing_data(connection, favorite_genre)
