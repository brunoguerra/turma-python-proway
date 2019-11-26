def idade_valida(idade):
    return idade >= 18

def cadastro():
  nome = input('Digite o nome: ')
  idade = int(input('Digite a idade: '))
  if idade_valida(idade):
    print('Cadastrado com sucesso: ', nome)
    print('Idade: ', idade)
  else:
    print('Idade Inválida :c')

def opcoes():
  return int(input(
    "Digite umas das opções:\n"
    "1. Cadastro\n"
    "0. Sair\n"
  ))



# while opcao != 0:
def main():
  opcao = opcoes()
  if opcao == 1:
    cadastro()
  elif opcao != 0:
    print("Opção não encontrada.")
  if opcao != 0:
      main()
  else:
    print('saindo...')


# Começou
main()
# print('opção', opcao)