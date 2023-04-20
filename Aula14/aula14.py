import os

os.system('cls')

#Aula de While

#Inicialização de variável de controle

i=0

while i<=9:
    print(i)
    i=i+1
    #Para interromper o loop podemos utilizar o BREAK
    if i>=5:
        break
print("Fim do loop\n")


#Percorrendo uma lista de strings com o while
carros=['Gol', 'Fox', 'Saveiro', 'Tempra', 'Fusca']
a=0
tam = len(carros)

while a<tam:
    print(carros[a])
    a+=1

print('\nFim do Loop')
