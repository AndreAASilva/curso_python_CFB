import os

nomes = []
nome = input("Digite o nome: ")

while nome != 'sair':
    nomes.append(nome)
    nome= input('Digite o nome: ')

os.system('cls')

for x in (nomes):
    print(x)

print(len(nomes))
    
