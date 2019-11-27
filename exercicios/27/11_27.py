dados_validos = False

while not dados_validos:

    try:
        idade = int(input('Qual sua idade?'))
        horas = int(input('Que horas você vai entrar?'))

        dados_validos = True

        if idade >= 50 and horas <= 22:
            print('Entrada Gratuita')
        elif idade >= 50 and horas >= 23:
            print('Entrada com Desconto de 30%')
        elif idade >= 18 and idade <= 49 and horas >= 22:
            print('Entrada com Desconto de 20%')
        elif idade <= 18 and idade >= 49 and horas >= 23:
            print('Entrada com Valor Integral')
        elif idade <= 17 and idade > 0:
            print('Menor de idade não entra, volte daqui um tempo!')
        else:
            dados_validos = False
            print('Digite um número!')

    except:
        print('Digite um número!')
    