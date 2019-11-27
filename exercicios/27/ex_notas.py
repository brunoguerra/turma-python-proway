n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))

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