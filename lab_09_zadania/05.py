import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

zamowienia = pd.read_csv('zamowienia.csv', sep=";")

pomoc = (zamowienia.groupby([zamowienia.Sprzedawca]).agg({'Sprzedawca':['count']}))
pomoc.plot.bar()
plt.show()


