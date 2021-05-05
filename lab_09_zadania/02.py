import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


imiona = pd.read_excel('imiona.xlsx')

pomoc = imiona.groupby([imiona.Plec]).agg({'Liczba':['sum']})
pomoc.plot.bar()
plt.show()


