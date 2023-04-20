import os

os.system('cls')

#Matriz - List trabalha com uma linha e Matriz trabalha com dois índices que trabalha com linha e coluna

"""
carros=['HRV', 'Golf', 'Focus', 'Argo']
print(carros[2])

carros[3]='Saveiro'
carros.append('Celta')

for x in (carros):
    print(x)

"""

carros = [
    ['Modelo','HRV'],
    ['Fabricante','Honda'],
    ['Ano', '2016']
]

carros.append(['Cor','Prata'])

print(carros[3][0] + ' - ' + carros[3][1])


for x,y in (carros):
    print(x," | ",y)