import plotly.express as px
import pandas as pd

# ЗАДАНИЕ 1
# Словарь исходных данных
# Объект DataFrame
df = pd.DataFrame({
    'month': ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
              "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"],
    'month_num': list(range(1, 13)),
    'avg_temp': [-5, -5, -1, 5, 11, 16, 19, 17, 12, 6, 1, -2]
})

# Анимированный график
temp_min, temp_max = df['avg_temp'].min() - 5, df['avg_temp'].max() + 5
fig = px.bar(df,
             x='month',
             y='avg_temp',
             color='avg_temp',
             color_continuous_scale="Viridis",
             animation_frame='month_num',
             range_color=[temp_min, temp_max],
             labels={'avg_temp': 'Средняя температура, °C', 'month': '', 'month_num': 'Номер месяца'},
             title='Среднемесячная температура в Санкт-Петербурге за год')

fig.update_layout(
    title_font=dict(weight="bold"),
    title_x=0.5,
    yaxis_range=[temp_min, temp_max],
    yaxis_fixedrange=False
)
fig.show()