import random

f=open("alunos.txt", "r")

print('... sorteando')
if f.mode == 'r':
  contents =f.read()
  print(random.sample(contents.split("\n"), 1))

  