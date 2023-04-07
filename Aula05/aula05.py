#Tipos numéricos

import random

num_i = 10
num_f = 5.2
num_c = 1j #números complexos

#Após importar a biblioteca random, abaixo foi criada uma variável que vai gerar um valor aleatório com início em 0 até 59, inserimos o valor inicial e final.

# num_r = random.randrange(0,59)

num_r = [
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59)
    ]

print("Valor 1: " + str(num_r[0]))
print("Valor 2: " + str(num_r[1]))
print("Valor 3: " + str(num_r[2]))
print("Valor 4: " + str(num_r[3]))
print("Valor 5: " + str(num_r[4]))
print("Valor 6: " + str(num_r[5]))

# x=num_r

#É possível realizar a conversão direto na variável

"""
x = float(num_i)
x = int(num_f)
x = bool(num_i)
"""

#Para converter um inteiro com uma string utilizamos o STR()
#Neste exemplo antes de incluir os STRs() ele deu erros, pois não era possível concatenar números inteiros com tipos, ambos foram convertidos para está ação ser realizada

"""
print("Valor: " + str(x) + " - Tipo: " + str(type(x)))
print("Valor: " + str(x))
print(type(x))

"""

num_ran = [
    random.randrange(0,20),
    random.randrange(0,20),
    random.randrange(0,20)
]

print(num_ran[0])
print("Valor 01: " + str(num_ran[0]) + " - " + str(type(num_ran)))
print("Valor 02: " + str(num_ran[1]) + " - " + str(type(num_ran)))
print("Valor 03: " + str(num_ran[2]) + " - " + str(type(num_ran)))