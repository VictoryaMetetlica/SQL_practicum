from create_DT_trip import connection, execute_query, printing_data

print('\n Для каждого города посчитать, сколько раз сотрудники в нем были. Информацию вывести в отсортированном в алфавитном \
порядке по названию городов. Вычисляемый столбец назвать Количество.\n')

count_city_visited = """
	SELECT city, count(trip_id) AS Количество
	FROM trip
	GROUP BY city
	ORDER BY city ASC;
"""

    # comit() не выполняем, так как данные используются только для задачек, а изначальная таблица trip не меняется
printing_data(connection, count_city_visited)


print('\nВывести два города, в которых чаще всего были в командировках сотрудники. Вычисляемый столбец назвать Количество.')
two_favorite_cities = """
    SELECT city, count(trip_id) AS Количество
    FROM trip
    GROUP BY city
    ORDER BY Количество DESC
    LIMIT 2;
"""
printing_data(connection, two_favorite_cities)

print('Вывести информацию о командировках, начало и конец которых относятся к одному месяцу (год может быть любой). \
Результат отсортировать сначала в алфавитном порядке по названию города, а затем по фамилии сотрудника.')

one_month_trips = '''
    SELECT name, city, date_first, date_last
    FROM trip
    WHERE MONTH(date_first) = MONTH(date_last)
    ORDER BY 2 ASC, 1 ASC;
'''
printing_data(connection, one_month_trips)

print('\nВывести сумму суточных (произведение количества дней командировки и размера суточных) для командировок, \
первый день которых пришелся на февраль или март 2020 года. Значение суточных для каждой командировки занесено в столбец \
 per_diem. Информацию отсортировать сначала в алфавитном порядке по фамилиям сотрудников, а затем по убыванию суммы \
 суточных.')

february_march_money = '''
    SELECT name, city, date_first, (DATEDIFF(date_last, date_first) + 1) * per_diem AS Сумма
    FROM trip
    WHERE date_first >= '2020-02-01' AND date_first <= '2020-03-31' 
'''
printing_data(connection, february_march_money)

print('\n Вывести название месяца и количество командировок для каждого месяца. Считаем, что командировка относится к \
некоторому месяцу, если она началась в этом месяце. Информацию вывести сначала в отсортированном по убыванию количества,\
 а потом в алфавитном порядке по названию месяца виде. Название столбцов – Месяц и Количество.')

trips_in_month = '''
    select 
        monthname(date_first) as Месяц, 
        count(month(date_first)) as Количество
    from trip
    group by Месяц
    order by Количество desc, Месяц
'''
printing_data(connection, trips_in_month)

print('\n Вывести информацию о командировках сотрудника(ов), которые были самыми короткими по времени.')
short_trips = '''
    SELECT name, city, date_first, date_last
    FROM trip
    WHERE datediff(date_last, date_first) = (SELECT MIN(datediff(date_last, date_first)) FROM trip);
'''
printing_data(connection, short_trips)

print('\n Вывести информацию о командировках во все города кроме Москвы и Санкт-Петербурга (фамилии и инициалы сотрудников, \
 город , длительность командировки в днях, при этом первый и последний день относится к периоду командировки). Информацию \
 вывести в упорядоченном по убыванию длительности поездки, а потом по убыванию названий городов (в обратном алфавитном \
 порядке).')

exept_Moscov_Peter = '''
    SELECT name, city, datediff(date_last, date_first) + 1 AS Длительность
    FROM trip
    WHERE city NOT IN ('Москва', 'Санкт-Петербург')
    ORDER BY Длительность DESC, city DESC;
'''
printing_data(connection, exept_Moscov_Peter)