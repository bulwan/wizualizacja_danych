import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plik = pd.ExcelFile('imiona.xlsx')
imiona = pd.read_excel(plik,'Arkusz1')
pomoc=imiona.groupby([imiona.Plec]).agg({'Liczba':[sum]})

#wykres 1

a=int(pomoc.loc['K'])
b=int(pomoc.loc['M'])
plt.subplot(3,1,1)
etykiety = ['K', 'M']
wartosci = [a,b]
plt.yticks(np.arange(0, 4000000, 500000))
plt.bar(etykiety,wartosci)

#wykres 2

plt.subplot(3,1,2)
kobiet=imiona[(imiona.Plec=='K')]
chlopcy=imiona[(imiona.Plec=='M')]
wynik_dziewczynki = kobiet.groupby(['Rok']).sum()
wynik_chlopcy = chlopcy.groupby(['Rok']).sum()
wynik_dziewczynki=wynik_dziewczynki.reset_index()
wynik_chlopcy=wynik_chlopcy.reset_index()
plt.xticks(np.arange(2000, 2018, 1))
plt.plot(wynik_dziewczynki.Rok,wynik_dziewczynki.Liczba, label="dziewczynki")
plt.plot(wynik_chlopcy.Rok,wynik_chlopcy.Liczba, label="chlopcy")
plt.legend()

#wykres 3

plt.subplot(3,1,3)
dzieci = imiona.groupby(['Rok']).sum()
dzieci = dzieci.reset_index()
plt.xticks(np.arange(2000, 2018, 1))
plt.bar(dzieci.Rok, dzieci.Liczba)


plt.show()
