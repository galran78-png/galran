# import sqlite3
# import random
#
# # Исходные данные
# cities = ["Москва", "Санкт-Петербург", "Казань"]
# months = [
#     "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
#     "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
# ]
# # Подключение к БД
# conn = sqlite3.connect("sales.db")
# cursor = conn.cursor()
# # Создание таблицы
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS sales (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     city TEXT NOT NULL,
#     month TEXT NOT NULL,
#     amount REAL NOT NULL
# )
# """)
# # Генерация данных
# for city in cities:
#     for month in months:
#         amount = round(random.uniform(1, 50), 2)
#         cursor.execute(
#             "INSERT INTO sales (city, month, amount) VALUES (?, ?, ?)",
#             (city, month, amount)
#         )
# conn.commit()
# # Закрытие соединения
# conn.close()
# print("База данных успешно создана и наполнена")

import sqlite3
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html

# Первичная загрузка данных из БД
conn = sqlite3.connect("sales.db")
df_all = pd.read_sql("SELECT city, month, amount FROM sales", conn)
conn.close()

# Выбор столбца для фильтрации
by_column = "city"  # имя столбца, по которому фильтруем
filter_by = df_all[by_column].drop_duplicates().sort_values().tolist() # список значений для фильтрации

# Инициализация приложения и layout
app = Dash(__name__)

header = html.H3(
    "Динамика продаж по месяцам",
    style={'textAlign': 'center', 'margin': '0 0 20px 0'}
)

dropdown = dcc.Dropdown(
    id="dropdown-sender-id",
    options=[{"label": val, "value": val} for val in filter_by],
    value=filter_by[0] if filter_by else None,
    clearable=False,
    style={'width': '300px'}
)

graph_component = dcc.Graph(id="dropdown-receiver-id")

# Макет приложения
app.layout = html.Div(children=[
    header,
    html.Div([
        html.Label('Выберите город:'),
        dropdown,
        graph_component
    ])
])

@app.callback(
    Output("dropdown-receiver-id", "figure"),
    Input("dropdown-sender-id", "value")
    )
def update_graph(selected_value):
    df_filtered = df_all[df_all[by_column] == selected_value].copy() # фильтруем
    fig = px.bar(df_filtered,
                 x='month',
                 y='amount',
                 labels={'month': 'Месяц', 'amount': 'Продажи, тыс. ₽'})
    return fig

if __name__ == '__main__':
     app.run(debug=True)