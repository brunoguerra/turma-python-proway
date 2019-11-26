p = [6,2,4,0,10,20,12,14,16,18]
q = [5,15,25,0,10,20]

intersecao = []
for item_p in p:
    if item_p in q:
        intersecao.append(item_p)

print(intersecao)