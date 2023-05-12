import os
import requests
import pandas as pd
import openpyxl
import datetime
from bs4 import BeautifulSoup

# отправляем запрос на получение HTML страницы и получаем ее содержимое
response = requests.get('https://rate.am/ru/armenian-dram-exchange-rates/banks/non-cash?tp=0&rt=1')
html = response.content
# используем BeautifulSoup для парсинга HTML кода
soup = BeautifulSoup(html, 'html.parser')

# ищем таблицы на странице
tables = soup.find_all('table')
# находим нужную таблицу по тексту
table = None
for t in tables:
    if 'Эвокабанк' in str(t):
        table = t
        df = pd.read_html(str(table))[0]  # Преобразуем таблицу в DataFrame
        break
df = df.drop(index=20, columns=[0, 2, 3, 13, 14])
df.loc[1][1] = 'Bank'
df.loc[1][4] = 'Дата'
df.loc[1][5] = 'USD buy'
df.loc[1][6] = 'USD sell'
df.loc[1][7] = 'Euro buy'
df.loc[1][8] = 'Euro sell'
df.loc[1][9] = 'RUR buy'
df.loc[1][10] = 'RUR sell'
df.loc[1][11] = 'GBP buy'
df.loc[1][12] = 'GBP sell'
df = df.drop(index=0)
# устанавливаем значения строки 0 в качестве заголовков столбцов dataframe
df.columns = df.iloc[0]
# удаляем первую строку, которую мы использовали как заголовок столбцов
df = df.drop(df.index[0])
# создаем маску для сортировки, сортировать будем только первые 19 строк, а остальные оставим неизмененными
mask = df.index < 20
# # сортируем данные по столбцу 'RUR buy' по убыванию
df_sorted = df[mask].sort_values(by='RUR buy', ascending=False)
# # объединяем DataFrame с отсортированными данными и оставшимися неизменными данными
df = pd.concat([df_sorted, df[~mask]])
print(df.reset_index, '\n')

# Указываем путь к файлу и его имя
path = input('Введите путь сохранения курса валют с Rate.am:')
# проверяем, что путь существует, если нет, создаем его
if not os.path.exists(path): os.makedirs(path)
# приводим путь к корректному виду
path = os.path.abspath(path)
# Проверяем, что путь заканчивается на "/"
if not path.endswith("/"): path += "/"
filename = f'amdkurs_{str(datetime.datetime.now().date())}_{str(datetime.datetime.now().time())[:2]}.xlsx'
# path = path + filename
path += filename

# Экспортируем датафрейм в Excel
df.to_excel(path, index=False)
