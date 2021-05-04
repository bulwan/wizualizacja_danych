import pandas as pd
import numpy as np

zamowienia = pd.read_csv('zamowienia.csv', sep=";")
print(zamowienia.nlargest(5, 'Utarg'))