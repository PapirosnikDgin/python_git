import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sb

__author__ = "Номокoнов"

# uniform значения действительных чисел из равномерного распределния все значения
# от low до high имеют одинаковый шанс выпадения, 3 параметр размер массива
a = np.random.uniform(0,100,(100) )

sb.histplot(a)
plt.show()