from console import print_color, print_color_bg

def idade_valida(idade):
    return idade >= 18

records = []

def cadastro():
  global records
  nome = input('Digite o nome: ')
  idade = int(input('Digite a idade: '))
  if idade_valida(idade):
    print('Cadastrado com sucesso: ', nome)
    print('Idade: ', idade)
  else:
    print('Idade Inválida :c')

  file_bd = 0
  try:
    file_bd = open('bancodedados.txt', 'r')
    contents = file_bd.read().split('\n')

    records = [line.strip().split(',') for line in contents]
    file_bd.close()
  except Exception as e:
    print('Error on open file', e)
    records = []

  duplicated = False

  for line in records:
    duplicated = duplicated or line[0] == nome
    
  if duplicated:
    raise Exception('Duplicated record')
  
  records.append([nome, str(idade)])

  file_bd = open('bancodedados.txt', 'w+')

  print('records ', records)
  for line in records:
    file_bd.write(','.join(line)+'\n')
  
  file_bd.close()


def opcoes():
  return int(input(
    "Digite umas das opções:\n"
    "1. Cadastro\n"
    "0. Sair\n"
  ))



# while opcao != 0:
def main():
  opcao = opcoes()
  try:
    if opcao == 1:
      cadastro()
    elif opcao != 0:
      print("Opção não encontrada.")

    if opcao != 0:
        main()
    else:
      print('saindo...')
  except Exception as e:
    print('Problem on option ', opcao, e)
    main()


# Começou
main()
# print('opção', opcao)