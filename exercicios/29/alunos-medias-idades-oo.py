# idades = []
# alturas = []

alunos = []

class Aluno:
    TOTAL_ALUNOS_CRIADOS = 0
    def __init__(self):
        Aluno.TOTAL_ALUNOS_CRIADOS += 1

    def set_idade(self, idade):
        self._idade = idade
    
    def get_idade(self):
        return self._idade

    def set_altura(self, altura):
        self._altura = altura
    
    def get_altura(self):
        return self._altura

aluno = Aluno()
aluno.set_idade(23)
aluno.set_altura(180)

soma_das_alturas = 0
for i in range(30):
  aluno = Aluno()
  valor_idade = int(input('Digite uma idade: '))
  aluno.set_idade(valor_idade)

  valor_altura = int(input('Digite uma altura(cm): '))
  aluno.set_altura(valor_altura)

  soma_das_alturas = soma_das_alturas + valor_altura

  alunos.append(aluno)

media_das_alturas = soma_das_alturas / len(alunos)

print('A média da altura dos alunos é', media_das_alturas)

quantos_inferiores_a_media = 0
#for i in range(len(alunos)):
#    if idades[i] >= 13 and alturas[i] < media_das_alturas:
for aluno in alunos:
    if aluno.get_idade() >= 13 and aluno.get_altura() < media_das_alturas:
        quantos_inferiores_a_media += 1

print(f'Total de alunos acima de 13 abaixo da média na altura {quantos_inferiores_a_media}')

print('TOTAL_ALUNOS_CRIADOS: ', Aluno.TOTAL_ALUNOS_CRIADOS)