#variáveis
# nomeVar = 2
# nomeVar = 2.777
# nomeVar = 'texto'













def opcoes():
  return int(input(
    "Digite umas das opções:\n"
    "1. Cadastro\n"
    "0. Sair\n"
  ))
opcao = opcoes()

print('opção', opcao)

while opcao != 0:
  if opcao == 1:
    cadastro()
  else:
    print("Opção não encontrada.")
  opcao = opcoes()