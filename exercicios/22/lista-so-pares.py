# Exercício: Criar uma lista com 10 números inteiros e preencher com a entrada do usuário com números e remover o impáres.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for l in lista:
    if (l % 2) == 1:
        lista.remove(l)

print("Primeira lista", lista)  

# for g in lista:

#     final = g * 2
#     lista.append(final)

# print(lista)
