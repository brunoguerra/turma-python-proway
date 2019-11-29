modelos = ['FUSCA', 'GOL', 'VECTRA', 'COROLA', 'S10']
km_per_l = [6, 15, 14, 18, 12]

economico = max(km_per_l)

for i in range(len(modelos)):
    if km_per_l[i] == economico:
        print('Modelo mais economico', modelos[i])

for i in range(len(modelos)):
    print(modelos[i], 'consome ', 1000 / km_per_l[i], 'L em 1000km')