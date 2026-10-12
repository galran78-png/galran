import matplotlib.pyplot as plt

# ЗАДАНИЕ 1
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
electronics = [40, 55, 48, 70]
clothing = [30, 45, 40, 65]
books = [15, 20, 18, 25]
colors = ['red', 'green', 'blue', 'cyan']
# построение диаграммы
plt.stackplot(quarters, electronics, clothing, books,
              labels=['Электроника', 'Одежда', 'Книги'], colors = colors)
# подписи и сетка
plt.legend(loc='upper left')
plt.title('Общие продажи')
plt.xlabel('Квартал')
plt.ylabel('Продажи')
plt.grid(True, linestyle='-', alpha=0.5)
# рамка
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
# показать всё
plt.show()