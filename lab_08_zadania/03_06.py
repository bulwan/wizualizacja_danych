import pandas as pd
import numpy as np

zamowienia = pd.read_csv('zamowienia.csv', sep=";")
zamowienia['Rok'] = pd.DatetimeIndex(zamowienia['Data zamowienia']).year
pomoc = zamowienia[(zamowienia.Rok==2004)].mean()
print(pomoc.Utarg)
