loja = {
    'perifericos': [500, 400, 300, 250, 200, 150],
    'gabinete': [1000, 900, 800, 650, 150],
    'tela': [2899, 120, 550, 2500, 1000, 350],
}

resultado = 0
for sla in loja.values():
    resultado += min(sla)
print(f'O resultado foi \033[1;32m{resultado}\033[m')
