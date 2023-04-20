import os

nomes = []
nome = input('Digite o nome do usuário: ')

while nome != 'sair':
    nomes.append(nome)
    nome=input('Digite o nome do usuário: ')
    
os.system('cls')

for x in (nomes):
    print(x)
    
