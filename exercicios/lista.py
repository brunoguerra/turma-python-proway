lista = [1,2,3,4,5,6,4,8,2]
# print(lista)
# for i in range(len(lista),0 ,-1):
#     if lista[i-1] % 2 != 0:
#         lista.remove(lista[i-1])
# print(lista)


for i in range(len(lista), 0 , -1):
    if lista[i-1] % 2 == 1:
        lista.remove(lista[i-1])

print(lista)        

#CreatedByYuriHartmann