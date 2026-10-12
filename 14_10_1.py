import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

# ЗАДАНИЕ 1
tips = sns.load_dataset('tips')
# построение диаграммы
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')
# подписи
plt.title('Зависимость чаевых от суммы счёта')
plt.xlabel('Сумма счёта')
plt.ylabel('Чаевые')
plt.legend(title='Пол клиента', labels=['Мужской', 'Женский'])
# вывод
plt.show()