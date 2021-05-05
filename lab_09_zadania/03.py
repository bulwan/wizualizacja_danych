import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


imiona = pd.read_excel('imiona.xlsx')

pomoc = imiona.groupby([imiona.Plec]).agg({'Liczba':['sum']})
pomoc.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.show()


