# rateam_loader. Загрузчик данных с сайта rate.am в excel-файл

**Задача**: Достать с сайта [rate.am](https://rate.am/ru/armenian-dram-exchange-rates/banks/non-cash) таблицу с курсом валют, отсортировать по убыванию курса покупки рубля банками и выгрузить в excel-файл. 

**Стек**: python, библиотеки pandas, bs4  

**Процесс**: На заданной странице ищется необходимая таблица, загружается в датафрейм, убираются лишние строки и столбцы, фрагмент датафрейма с курсами сортируется по убыванию курса покупки рубля банками, запрашивается путь для сохранения файла, проверяется на доступность, датафрейм выгружается в excel-файл, в имени которого указана текущая дата и время (часы).  


**Результат**: получился рабочий код, который я использовал некоторый период времени, есть планы переработки функцию.

Сurrency rate loader from rate.am
A data loader is used to download data from the rate.am website into an Excel file. On the page, the necessary table with currency exchange rates is searched for, unnecessary rows and columns are deleted, the appropriate headers are assigned to the columns, and the data is sorted by the ruble purchase rate offered by banks. The resulting dataframe is then exported to an Excel file.
