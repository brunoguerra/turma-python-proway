

arquivo = open('aula\\exercicios\\textao.txt', 'r')
arquivo_NO_LOREM = open('aula\\exercicios\\textao-nolorem.txt', 'w')
#contents = arquivo.read()
content = arquivo.read()
substituto = 'gohorse'

linhas = content.split('\n')
print('total de linhas', len(linhas))

total_de_palavras = 0
for linha in linhas:
  total_de_palavras += len(linha.split())
  linha_nova = linha.replace('lorem', substituto)
  linha_nova = linha.replace('Lorem', substituto.title())
  arquivo_NO_LOREM.write(linha_nova)
  arquivo_NO_LOREM.write('\n')

print('total de palavras', total_de_palavras)