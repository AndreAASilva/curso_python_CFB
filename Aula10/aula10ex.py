carros = ['Fusca', 'Celta', 'Gol', 'Focus']

print(carros)
print(carros[1])
print(len(carros))

if len(carros) >= 3:
    carros.append('Saveiro')
    print(carros)
else:
    print('Total insuficiente')


if 'Gol' in carros:
    print('Este carro está na lista')
else:
    print('Este carro não está na lista')
    
    

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
res = num1*num2

print('{} x {} = {}'. format(num1,num2,res))

