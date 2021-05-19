import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

zamowienia = pd.read_csv('zamowienia.csv', sep=";")

wynik = zamowienia.groupby([zamowienia.Sprzedawca]).count()
wynik = wynik.reset_index()
explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,)
wedges, texts, autotexts = plt.pie(wynik.Utarg, explode=explode,  shadow=True, labels=wynik.Sprzedawca, autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"))
plt.legend(bbox_to_anchor=(-0.05, 0.4), loc=4)
plt.title('Sprzedawcy')

plt.show()

