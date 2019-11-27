

arquivo = open('aula\\exercicios\\textao.txt', 'r')
arquivo_NO_LOREM = open('aula\\exercicios\\textao.txt', 'w')
#contents = arquivo.read()
content = arquivo.read().lower()
print(content.count('lorem'))
print(content.count('ipsum'))

linhas = content.split('\n')
print('total de linhas', len(linhas))
# print('Total de palavras da primeira linhas', linhas[0].split())

total_de_palavras = 0
for linha in linhas:
  total_de_palavras += len(linha.split())
  arquivo_NO_LOREM.write(linha.replace())
print('total de palavras', total_de_palavras)


lorem_total = 0
ipsum_total = 0
for linha in linhas:
    words = linha.split()
    for word in words:
        if 'lorem' in word:
            lorem_total += 1
        if 'ipsum' in word:
            ipsum_total += 1

print('total de lorems', lorem_total)
print('total de ipsum', ipsum_total)
print(linhas[0].split())
# words = [linha.split() for linha in linhas]
# print(len(words))