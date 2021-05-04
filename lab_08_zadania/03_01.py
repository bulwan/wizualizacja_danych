import pandas as pd
import numpy as np

zamowienia = pd.read_csv('zamowienia.csv', sep=";")
print(pd.DataFrame(zamowienia.Sprzedawca.unique()))