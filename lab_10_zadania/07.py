import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plik = pd.ExcelFile('imiona.xlsx')
imiona = pd.read_excel(plik,'Arkusz1')


kobiet=imiona[(imiona.Plec=='K')]
chlopcy=imiona[(imiona.Plec=='M')]
wynik_dziewczynki = kobiet.groupby(['Rok']).sum()
wynik_chlopcy = chlopcy.groupby(['Rok']).sum()
wynik_dziewczynki=wynik_dziewczynki.reset_index()
wynik_chlopcy=wynik_chlopcy.reset_index()
plt.xticks(np.arange(2000, 2018, 1))
plt.bar(wynik_dziewczynki.Rok,wynik_dziewczynki.Liczba, label="dziewczynki", color='pink')
plt.bar(wynik_chlopcy.Rok,wynik_chlopcy.Liczba, label="chlopcy", color='blue', bottom=wynik_dziewczynki.Liczba)
plt.legend()
plt.show()