import pandas as pd
import numpy as np
import xlrd
import openpyxl

imiona = pd.read_excel('imiona.xlsx')
print(imiona[(imiona.Imie =="JOANNA")])

