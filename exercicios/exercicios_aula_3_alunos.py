lista_nomes = []

for i in range(10):
    nomes = input('Digite um nome: ')
    invertido = nomes[::-1]
    lista_nomes.append(invertido)
print(lista_nomes)