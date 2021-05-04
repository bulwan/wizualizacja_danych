import pandas as pd
import numpy as np

zamowienia = pd.read_csv('zamowienia.csv', sep=";")
zamowienia['Rok'] = pd.DatetimeIndex(zamowienia['Data zamowienia']).year
pomoc4 = zamowienia[(zamowienia.Rok==2004)]
pomoc5 = zamowienia[(zamowienia.Rok==2005)]
pomoc4.to_csv('zamowienia_2004.csv', sep=";", index=False)
pomoc5.to_csv('zamowienia_2005.csv', sep=";", index=False)