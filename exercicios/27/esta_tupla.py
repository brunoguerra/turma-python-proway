permissao = (int, float)

def teste(msg):
    if type(msg) in permissao:
        return "Isso está na lista de permissões!"
    else:
        raise Exception("Isso não está na lista de permissões!")

print(teste("OIIII"))