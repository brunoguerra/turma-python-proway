x = int(input('Digite o primeiro valor: '))
z = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))

if x < y and x < z:
    print('X é menor')
elif z < y:
    print('Z menor')
else:
    print('Y menor')