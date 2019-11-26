def pega_int(message):
    while True:
        try:
            i = int(input(message))
            print('Número é ', i)
        except:
            print('Digite um número válido')
        else:
            return i

valorInt = pega_int('Digite um número')

print(valorInt)
