import os
import random

print([random.random() for x in range(10)])

ext = 'py'
def isPy(arquivo):
    return arquivo[-2:] == ext

path = "C:\\Users\\hbsis\\Documents"
arquivos = os.listdir(path)
for arquivo in arquivos:
    print(arquivo)

os_pys = list(filter(isPy, arquivos))
print('============= === ===============')
for arquivo in os_pys:
    print(arquivo)


def esseArquivoEhDiretorio(arquivo):
    return len(arquivo.split('.')) == 1


os_pys = list(filter(esseArquivoEhDiretorio, arquivos))
print('============= === ===============')
for arquivo in os_pys:
    print(arquivo)
