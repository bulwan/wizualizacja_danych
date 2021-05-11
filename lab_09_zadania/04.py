import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed()
data = pd.read_csv('iris.data')
data.columns=['sepal length in cm',  'sepal width in cm', 'petal length in cm', 'petal width in cm', 'clas']
kwiat1 = data[data.clas=='Iris-setosa']
kwiat2 = data[data.clas=='Iris-versicolor']
kwiat3 = data[data.clas=='Iris-virginica']
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(kwiat1['sepal length in cm'],kwiat1['sepal width in cm'], color='red', marker='^')
ax1.scatter(kwiat2['sepal length in cm'],kwiat2['sepal width in cm'], color='blue', marker=',')
ax1.scatter(kwiat3['sepal length in cm'],kwiat3['sepal width in cm'], color='magenta', marker='>')
# kwiat2.plot.scatter('sepal length in cm', 'sepal width in cm', color='blue')
# kwiat3.plot.scatter('sepal length in cm', 'sepal width in cm', color='yellow')
plt.grid(True)
plt.show()


