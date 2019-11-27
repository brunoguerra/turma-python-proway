print(format(' Boletim Escolar ', '=^60'), end='\n\n')

while True:
    qtd = input(f'Digite a qtd de notas: ')
    try:
        qtd = int(qtd)
    except:
        print('Digite um número: ')
    else: 
        break

notas = []

for i in range(qtd):
    while True:        
        n = input(f'Digite a nota {i +1} : ')
        try:
            n = float(n)
        except:
            print('Digite um número')
        else:
            if n <= 10 and n >= 0:
                notas.append(n)
                break
            else:
                print('Nota inválida!')

media = sum(notas) / len(notas)

print(f'Sua nota foi {media:.2f}')

if media >= 7 and media < 10:
    print('Aprovado!')
elif media == 10:
    print('Aprovado com distinção! Parabéns!')
else:
    print('Reprovado. Tente novamente ano que vem!')



#     Colete 3 notas do usuário, mais uma nota do trabalho, caso a médias das notas seja menor ou igual a 7.
# Caso a média das provas seja menor que 7 e o trabalho maior do que 8, exiba que o aluno está Aprovado da recuperação.

# Caso a média das provas seja menor que 7 e o trabalho menor que 8, exiba que o aluno está Reprovado.

# Caso a média das provas seja maior ou igual que 7, exiba que o aluno foi aprovado.

# Caso a média seja igual a 9, parabenize a dedicação e o sucesso do aluno.

# Se a média das provas for 10, informe que ele estará no Hall of fame of Python.


n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a terceira nota: '))
n3 = int(input('Digite a segunda nota: '))

trabalho = int(input('Digite a nota do trabalho: '))


media = (n1 + n2 + n3) / 3

if media < 7 and trabalho > 8:
    print('O aluno está aprovado da recuperação!')
if media < 7 and trabalho < 8:
    print('o aluno foi aprovado!')
if media >= 7:
    print('o aluno foi aprovado')  
if media == 9:
    print('parabéns amigo, você é um amigo!')
elif media == 10:
    print('você está no hall of fame of python!')              