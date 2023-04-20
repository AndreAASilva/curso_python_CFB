import os

nomes = []
sobre_nome = []
nome = input('Digite o nome: ')
sobre = input('Digite o sobrenome: ')

while nome != 'sair':
    nomes.append(nome)
    nome = input('Digite o nome: ')
    
    sobre_nome.append(sobre)
    sobre = input('Digite o sobrenome: ')
    
os.system('cls')

print('Meu nome é: {} e o sobrenome: {}'. format(nomes[0], sobre_nome[0]))
print('Meu nome é: {} e o sobrenome: {}'. format(nomes[1], sobre_nome[1]))
print('Meu nome é: {} e o sobrenome: {}'. format(nomes[2], sobre_nome[2]))

