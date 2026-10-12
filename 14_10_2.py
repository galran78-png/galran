import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# ЗАДАНИЕ 2
tips = sns.load_dataset('tips')
# построение диаграммы
sns.boxplot(data=tips, x='smoker', y='total_bill')
# подписи
plt.title('Распределение общего счёта по статусу курения')
plt.xlabel('Курящий')
# Замена ярлыков на русские
locs, labels = plt.xticks()
new_labels = ['Да', 'Нет']
plt.xticks(locs, new_labels)
plt.ylabel('Общий счёт')
# вывод
plt.show()