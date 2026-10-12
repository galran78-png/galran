import matplotlib.pyplot as plt
import seaborn as sns

# ЗАДАНИЕ 3
iris = sns.load_dataset('iris')

# вычисление корреляций (Pearson)
corr_matrix = iris.corr(numeric_only=True)
#print(corr_matrix)
# построение диаграммы
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, linecolor="gray", square=True)
# подписи
ax.set_title('Матрица корреляции в датасете Iris', fontsize=14, fontweight="bold")
plt.tight_layout()
# вывод
plt.show()