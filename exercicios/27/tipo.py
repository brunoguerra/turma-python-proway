# Crie um script que declare uma função, receba um parâmetro e diga o tipo que foi passado em uma mensagem.

def mostrar_tipo(menssagem):
        if type(menssagem) is int:
            return 'Isso é um número inteiro'
        if type(menssagem) is float:
            return 'Isso é um número decimal'
        if type(menssagem) is str:
            return 'Isso é uma linha de texto'


print(mostrar_tipo(6876))
print(mostrar_tipo('6876'))
print(mostrar_tipo(6876.777))