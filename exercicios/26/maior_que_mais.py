n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

# if n1 < n2 > n3:
#     print(n2)
# elif n2 < n3 > n1:
#     print(n3)
# else:
#     print(n1)

if n1 > n2 and n1 > n3:
  print('n1')
elif n2 > n3:
  print('n2')
else:
  print('n3')


