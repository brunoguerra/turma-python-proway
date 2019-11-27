import sys

alunos = [
    { 'nome': 'William perna curta', 'idade': 18},
    { 'nome': 'Andrei com fome', 'idade': 19}
]

menorIdade = sys.maxsize
indexMenorIdade = 0
i = 0
for aluno in alunos:
    if aluno['idade'] < menorIdade:
        menorIdade = aluno['idade']
        indexMenorIdade = i
    i += 1

alunos.pop(indexMenorIdade)

print(alunos)