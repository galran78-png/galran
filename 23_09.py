import numpy as np

# 1
x = np.arange(10, 50, 5)
print(x)

# 2
x = np.random.randint(0, 11, size=(3, 4))
print(x)
print('Форма:', x.shape)
print('Размер:', x.size)
print('Тип данных:', x.dtype)

# 3
x = np.ones((4,4), dtype=int)
print(x)
x[0] = 0
print(x)

# 4
x = np.random.randint(0, 11, size=(3, 3))
print(x)
print('Сумма:', x.sum())
print('Среднее по строкам:', np.round(x.mean(axis=1), 1))
print('Среднее по столбцам:', np.round(x.mean(axis=0), 1))

# 5
x = np.array([8500, 12000, 4300, 9100, 11500, 15000, 6000])
print('Минимальное количество шагов:', x.min())
print('Максимальное количество шагов:', x.max())
print('Сумма всех шагов за неделю:', x.sum())

# 6
x = np.array([18.2, 19.5, 21.0, 17.8, 16.5,
              23.1, 24.5, 20.0, 19.1, 18.0,
              22.4, 25.0, 15.8, 17.2])
print('Средняя температура:', np.round(x.mean(), 1))
print('Медиана:', np.round(np.median(x), 1))
print('SD:', np.round(np.std(x), 1))
print('Дисперсия:', np.round(np.var(x), 1))

# 7
x = np.array([30, 35, 40, 45, 300])
print('Средняя зарплата:', np.round(x.mean(), 1))
print('Медиана:', np.round(np.median(x), 1))

# 8
x = np.array([150, 142, 165, 139, 155])
print('Дешевле всего:', np.argmin(x))
print('Дороже всего:', np.argmax(x))








