
import seaborn as sb
import numpy as np 
import matplotlib.pyplot as plt

__author__ = "Номокoнов"

# создание рандомных данные для занесение в heatmap
a = np.random.randint( 0, 10, size=(7,7) )
# создание heatmap на основе данных a cmap - вид heatmap представляет собой температуру
# annot - выводит значения яйчеек матрицы
sb.heatmap(a, cmap=sb.color_palette("rocket", as_cmap=True), annot = True)
# plt.show средство для вывода графика
plt.show()