import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# ЗАДАНИЕ 1
# массивы для городов
city_A = [20, 22, 19, 23, 25]
city_B = [15, 17, 18, 16, 21]
# массив дней недели
days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт']
# построение линий
ax.plot(days, city_A, '-or', label='Город A')
ax.plot(days, city_B, '-.sg', label='Город B')
# легенда и сетка
ax.set_xlabel('День', fontweight='bold')
ax.set_ylabel('Температура', fontweight='bold')
ax.legend()
ax.grid(True, linestyle='-', alpha=0.5)
# рамка
fig.gca().spines['top'].set_visible(False)
fig.gca().spines['right'].set_visible(False)
# показать всё
plt.show()