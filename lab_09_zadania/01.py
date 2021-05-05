import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


imiona = pd.read_excel('imiona.xlsx')
pomoc = imiona.groupby([imiona.Rok]).agg({'Liczba':['sum']})
pomoc.plot()
plt.show()