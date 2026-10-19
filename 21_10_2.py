# ИМПОРТ
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# ПОДГОТОВКА ДАННЫХ

# Данные
xs = list(range(1, 6))
ys = [x**2 for x in xs]
# DataFrame
df = pd.DataFrame({'x': xs, 'y': ys})
# График
fig = px.line(
    df,
    x='x',
    y='y',
    markers=True,
    title='График функции y = x²',
    labels={'x': 'Значение x', 'y': 'Значение y'}
)

# DASH

# app как объект класса Dash
app = Dash(__name__)

# Компоненты
header = html.H1(
    "Мой первый дашборд",
    style={"textAlign": "center", "margin": "0 0 20px 0"}
)
graph = dcc.Graph(figure=fig)

# Макет приложения
app.layout = html.Div(
    children=[header, graph],
    style={"fontFamily": "Arial, sans-serif", "padding": "30px"}
)

# Запустить Dash
if __name__ == '__main__':
    app.run(debug=True)