def menu(**rzeczy):
	return sum([int(value) for value in rzeczy.values()])

print(menu(maslo=2, bulka=3))