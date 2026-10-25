# ИМПОРТ
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Данные
data = {
    'categories': ['Авиация', 'Гражданская техника', 'Корабли', 'Модельная химия', 'Дополнения из смолы'],
    'sales': [20, 10, 3.2, 9.5, 5]
}
# DataFrame
df = pd.DataFrame(data)
# Графики
line_fig = px.line(
    x=data['categories'],
    y=data['sales'],
    markers=True,
    labels={'x': 'Категория', 'y': 'Продажи, тыс. ₽'}
)
bar_fig = px.bar(
    df,
    x='categories',
    y='sales',
    color='categories',
    labels={'categories': 'Категория', 'sales': 'Продажи, тыс. ₽'},
    template='plotly_white'
)

# DASH-ИНТЕРФЕЙС
# app как объект класса Dash
app = Dash(__name__)
# Компоненты
# Заголовок
header = html.H1(
    "Продажи магазина «Моделист» по категориям",
    style={'textAlign': 'center', 'margin': '0 0 20px 0'}
)
# Переключатели
radio_buttons = dcc.RadioItems(
    options= [
    {'label': 'Столбчатая диаграмма', 'value': 'bar'},
    {'label': 'Линейный график', 'value': 'area'}
],
    value='bar',  # по умолчанию диаграмма
    id='chart-type-radio',
    labelStyle={'display': 'inline-block', 'marginRight': '15px'}
)
#График
graph_component = dcc.Graph(id='main-graph',
                            figure=bar_fig, # по умолчанию диаграмма
                            style={'height': '400px'})

# Макет приложения
app.layout = html.Div(children=[
    header,
    html.Div([
        html.Label('Выберите тип графика:'),
        radio_buttons,
    ], style={'marginBottom': '20px'}),
    graph_component
])

# УПРАВЛЕНИЕ
@app.callback(
    Output('main-graph', 'figure'),
    Input('chart-type-radio', 'value')
)
def update_graph(chart_type):
    if chart_type == 'area':
        return line_fig
    elif chart_type == 'bar':
        return bar_fig
    else:
        return bar_fig  # На случай непредвиденного значения

#ЗАПУСК ПРИЛОЖЕНИЯ
if __name__ == '__main__':
    app.run(debug=True)