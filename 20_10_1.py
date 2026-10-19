import plotly.express as px

# ЗАДАНИЕ 1
df=px.data.gapminder()
df_canada = df[df['country'] == 'Canada']
fig = px.bar(
    df_canada,
    x = 'year',
    y = 'pop',
    title='Население Канады по годам',
    labels={'year': 'Год', 'pop': 'Население'},
    color_discrete_sequence=['steelblue']
)
fig.update_layout(xaxis_tickangle=-45,
                  title_font = dict(size=20, family="Arial", weight="bold"),
                  title_x=0.5
                  )
fig.show()