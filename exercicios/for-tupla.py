numeros = []
for i in range(10):
  numeros.append(int(input('numero')))

# maximo = numeros[0]
# for numero in numeros:
#   if numero > maximo:
#     maximo = numero

# print(maximo)

print(max(tuple(numeros)))
print(min(tuple(numeros)))
print(sum(numeros)/len(numeros))
