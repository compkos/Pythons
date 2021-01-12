lista = [67, 13, 32, 24, 2, 54, 19, 90, 77, 49]
num_len = len(lista)
print('Αρχική λίστα', lista)
for x in range(num_len - 1):
    for y in range(0, num_len - 1 - x):
        if lista[y + 1] < lista[y]:
            lista[y], lista[y + 1] = lista[y + 1], lista[y]
print('Τελική λίστα', lista)
