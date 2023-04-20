import os

os.system('cls')

#Tuplas em Python - Diferenç de uma lista para uma tupla
'''
Na tupla utilizamos parênteses ( )
Na tupla utilizamos colchetes [ ]
'''
t_carros = ('celta', 'gol', 'fox')
l_carros = ['celta', 'gol', 'fox']

#modificando item da list
# l_carros[2] = 'saveiro'

#modificando item da tupla
l_carros=list(t_carros)
l_carros[1]='saveiro'
t_carros=tuple(l_carros)

for x in (l_carros):
    print(x)
    
