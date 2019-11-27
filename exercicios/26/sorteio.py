import random
import time

f=open("alunos.txt", "r")

print('\033[1;34m' + format(" SORTEANDO ", '.<20') + '\033[m', end='\n\n')
time.sleep(2)

if f.mode == 'r':
  contents = f.read()
  print('\033[1;32m' + format((random.sample(contents.split("\n"), 1)[0]).title(), '^30') + '\033[m')

print('\n')  
