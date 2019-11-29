lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
lista_result = []
# print(lista.count(lista[0]))

for i in lista:
    if i < 0:
        lista_result.append(i)
print(sum(lista_result))        