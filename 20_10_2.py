import plotly.express as px

#ЗАДАНИЕ 2
df=px.data.tips()
fig = px.sunburst(df, path=['smoker', 'time', 'day'],
                  values='total_bill',
                  color='total_bill',
                  color_continuous_scale='RdBu',
                  labels={'total_bill': 'Total bill'},
                  title='Total Bills vs. Time/Smoking Status')
# Форматирование
fig.update_layout(title_font = dict(size=20, family="Arial", weight="bold"),
                  title_x=0.5,
                  margin=dict(l=20, r=20, t=60, b=20),
                  template='plotly_white'
                  )
fig.show()