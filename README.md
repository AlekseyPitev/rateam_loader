# rateam_loader. Загрузчик данных с сайта rate.am в excel-файл

**Задача**: Достать с сайта [rate.am](https://rate.am/ru/armenian-dram-exchange-rates/banks/non-cash) таблицу с курсом валют, отсортировать по убыванию курса покупки рубля банками и выгрузить в excel-файл. 

**Стек**: python, библиотеки pandas, requests, bs4  

**Процесс**: На заданной странице ищу необходимаю таблицу, загружаю её в датафрейм, убираю лишние строки и столбцы, фрагмент датафрейма с курсами сортирую по убыванию курса покупки рубля банками, запрашиваю пользователя путь для сохранения файла, проверяю его на доступность, и выгружаю датафрейм в excel-файл, в имени которого строится по шаблону amdkurs_[текущая дата]_[текущее время (часы)].  


**Результат**: получился рабочий код, который я использовал некоторый период времени для сранения в динамике курса рубля к драму и получения информации в каком из банков  курс наиболее выгодный. Есть планы переработки кода в функцию.

Сurrency rate loader from rate.am
A data loader is used to download data from the rate.am website into an Excel file. On the page, the necessary table with currency exchange rates is searched for, unnecessary rows and columns are deleted, the appropriate headers are assigned to the columns, and the data is sorted by the ruble purchase rate offered by banks. The resulting dataframe is then exported to an Excel file.
