import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# ЗАДАНИЕ 1
area = [35, 42, 54, 62, 71, 85, 93, 104, 115, 128]
price = [8.4, 11.3, 14.6, 19.8, 22.1, 28.9, 33.5, 41.6, 49.5, 58.9]
# построение графика
ax.scatter(area, price, color = 'b', marker='o', alpha=0.3)
# подписи и сетка
ax.set_xlabel('Площадь, кв. м', fontweight='bold')
ax.set_ylabel('Цена, млн. руб.', fontweight='bold')
ax.title.set_text('Стоимость и площади квартир')
ax.grid(True, linestyle='-', alpha=0.5)
# рамка
fig.gca().spines['top'].set_visible(False)
fig.gca().spines['right'].set_visible(False)
# показать всё
plt.show()