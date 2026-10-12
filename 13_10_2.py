import matplotlib.pyplot as plt

# ЗАДАНИЕ 2
brands = ['Apple', 'Samsung', 'Xiaomi', 'Другие']
market_share = [30, 25, 20, 25]

# построение диаграммы
plt.pie(market_share, labels=brands, autopct='%1.1f%%')
# подписи
plt.title('Доли рынка смартфонов')

# показать всё
plt.show()