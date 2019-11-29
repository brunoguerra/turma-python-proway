idades = []
alturas = []

for i in range(30):
  valor_idade = int(input('Digite uma idade: '))
  idades.append(valor_idade)

  valor_altura = int(input('Digite uma altura(cm): '))
  alturas.append(valor_altura)

media_das_alturas = sum(alturas) / len(alturas)

print('A média da altura dos alunos é', media_das_alturas)

quantos_inferiores_a_media = 0
for i in range(len(alturas)):
    if idades[i] >= 13 and alturas[i] < media_das_alturas:
        quantos_inferiores_a_media += 1

print(f'Total de alunos acima de 13 abaixo da média na altura {quantos_inferiores_a_media}')

