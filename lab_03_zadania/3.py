menu = {'jajka': 'sztuki', 'maka': 'kilogramy', 'kapusta': 'sztuki', 'czosnek': 'sztuki'}
lista = [x for x in menu.items() if "sztuki" in x] 
print(lista)