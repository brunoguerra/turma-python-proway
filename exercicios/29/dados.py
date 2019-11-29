# lista = [(i % 6) + 1 for i in range(100)]
# # lista2 = []
# for g in range(1, 7):
#     print("O valor", g, "apareceu ", lista.count(g))

from random import randint

lista = []

# Gera 100 números aleatórios
for i in range(100):
    lista.append(randint(1, 6))

for g in range(1, 7):
    print("O número", g, "apareceu", lista.count(g), "vezes")