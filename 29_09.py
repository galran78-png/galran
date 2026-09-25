import pandas as pd

# 1
data = pd.Series([12, 15, 8, 20, 25, 30, 10],
                 index=['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
                 )
print(data)
print('*' * 10)
print('Продажи более 15 тысяч:')
print(data[data > 15])
print('*' * 10)

# 2
data = pd.Series([85, 90, 78, 92, 88, 76, 95, 92],
                 index=['Аня', 'Боря', 'Влад', 'Глаша', 'Дима', 'Ева', 'Жора', 'Зина'])
print(data)
print('*' * 10)
print('3 самые высокие оценки:')
print(data.nlargest(3, keep='all') )
print('*' * 10)

# 3
data = pd.Series([16, 25, 38, 17, 42, 15])
major = data > 18
print(major)
print('*' * 10)
