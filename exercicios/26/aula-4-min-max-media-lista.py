lista = []

for i in range(5):
  lista.append(int(input('Digite um número: ')))
print(max(lista))
print(min(lista))
print(sum(lista) / len(lista))