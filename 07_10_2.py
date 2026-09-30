import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# ЗАДАНИЕ 2
x = ['Электроника', 'Одежда', 'Книги', 'Дом и сад']
y = [450, 320, 180, 290]
colors = ['red', 'green', 'blue', 'cyan']
# построение диаграммы
ax.bar(x, y, width = 0.6, color = colors)
# подписи и сетка
ax.set_ylabel('Продажи')
ax.title.set_text('Итоги продаж')
ax.grid(True, linestyle='-', alpha=0.5, axis='y')
# рамка
fig.gca().spines['top'].set_visible(False)
fig.gca().spines['right'].set_visible(False)
# показать всё
plt.show()