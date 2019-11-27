nomes = []

n = int(input('Quantos numeros vc deseja digitar?'))

i = 0
while i < n:
    nome = input('digite o nome: ')
    nomes.append(nome)
    i += 1

nomes = [nome[-1] + nome[1:-1] + nome[0] for nome in nomes]

print(nomes)