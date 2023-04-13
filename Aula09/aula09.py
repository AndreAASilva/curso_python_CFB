#Listas - Array

carros =  ['HRV', 'Golf', 'Argo', 'Focus']

#Trocando item da lista
carros[3] = "Fusca"

#Adicionando itens a lista com o append() (Acrescentar)

carros.append('Gol')
carros.append('Focus')
carros.append('Celta')

#Verificando o tamanho da lista
print(str(len(carros)) + ' carros na lista')
print(len(carros), "carros na lista")

#removendo itens da lista

carros.remove('Gol')
print('Agora há', len(carros), 'na lista')


#Método POP remove o último elemento da lista

carros.pop()

#DEL remove um item da lista informado pela posição

del carros[3]

#CLER limpa todos os elementos da lista

# carros.clear()

#Copiando uma lista para outra - Primeira forma apresnetada na aula
carros2 = list(carros)

#segunda forma mais direta
carros2 = carros

print('A lista nova tem', len(carros2), 'carros')




print(carros)
print(carros[0:4])


#Criando nova lista e vinculando duas listas em uma nova

carros3 = ['carro01', 'carro02', 'carro03']

nova_lista = carros2 + carros3

print(nova_lista)
print('A lista nova tem um total de', len(nova_lista), 'carros')

print(nova_lista[5])
