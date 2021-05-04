import pandas as pd
import numpy as np

zamowienia = pd.read_csv('zamowienia.csv', sep=";")
zamowienia['Rok'] = pd.DatetimeIndex(zamowienia['Data zamowienia']).year
print(zamowienia[(zamowienia.Rok==2005) & (zamowienia.Kraj=="Polska")].agg({'Sprzedawca':['count']}))
