import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

# ЗАДАНИЕ 2
# массив дохода
income = [120, 150, 90, 210, 180, 250]
# массив индексов
x = np.arange(len(income))
# x и y точки максимального значения
max_id = np.argmax(income)
max_val = income[max_id]
# построение линии
ax.plot(x, income, color='purple', linewidth=3)
# выделение максимального значения
plt.scatter(max_id, max_val, s=100, zorder=5, color='red')
# преобразование индексов в месяцы
ax.set_xticks(x, labels=[str(i + 1) for i in x])
# легенда, сетка, заголовок
ax.set_xlabel('Месяц', fontweight='bold')
ax.set_ylabel('Доход', fontweight='bold')
ax.title.set_text('Доход за 6 месяцев')
ax.grid(True, linestyle='-', alpha=0.5)
# рамка
fig.gca().spines['top'].set_visible(False)
fig.gca().spines['right'].set_visible(False)
# показать всё
plt.show()