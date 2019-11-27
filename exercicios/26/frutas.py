frutas_deposito = {'maracuja':1, 'goiaba':2, 'pitaya':3}

frutas_escolha = input('Nome da fruta:')

# if frutas_escolha in frutas_deposito:
try:
    print('Código:', frutas_deposito[frutas_escolha])
except Exception as e:
    print(e)
# else:
#     print('Sem estoque de', frutas_escolha)