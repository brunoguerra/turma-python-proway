investigacao = ('Telefonou para a vítima? ',
                'Esteve no local do crime? ',
                'Mora perto da vítima? ',
                'Devia para a vítima? ',
                'Já trabalhou com a vítima? ',)
quantidade_s = 0
# for i in lista vai trazer um por um, se eu colocar um input vai seguir a ordem
print('\033[4;1;33mVocê está em uma investigação, para o seu bem digite apenas "s" ou "n"\033[m')



for pergunta in investigacao:
    # resposta = recebe_s_ou_n(f'\033[1;31m{pergunta}\033[m')
    resposta = input(pergunta)
    # if resposta in 'sS':
    # if resposta.lower() == 's':
    if resposta == 's' or resposta == 'S':
        quantidade_s += 1

if quantidade_s == 2:
    print('Você foi classificado(a) como SUSPEITO!')
elif quantidade_s >= 3 and quantidade_s <= 4:
    print('\033[1;32mVocê foi classificado(a) como \033[1;33mCÚMPLICE!\033[m ')
elif quantidade_s == 5:
    print('\033[1;32mVocê é o \033[1;31mASSASINO!\033[m')
else:
    print('\033[1;37mVocê é INOCENTE\033[m')
