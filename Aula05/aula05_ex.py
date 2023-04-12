import random

num = [10, 11, 12, 13, 15]

num_ale = [
    random.randrange(0,10),
    random.randrange(0,10),
    random.randrange(0,10),
    random.randrange(0,10),
    random.randrange(0,10)
]

print(num_ale[0])
print(num_ale[1])
print(num_ale[2])
print(num_ale[3])
print(num_ale[4])

print('Um dos valores da lista é:', num[3], 'e o outro é:' ,num[1])


num_ale2 = [
    random.randrange(0,100),
    random.randrange(0,100),
    random.randrange(0,100),
    random.randrange(0,100),
    random.randrange(0,100),
    random.randrange(0,100)
]

print('O primeiro valor é:', num_ale2[0])
print('O segundo valor é:', num_ale2[1])
print('O terceiro valor é:', num_ale2[2])
print('O quarto valor é:', num_ale2[3])
print('O quinto valor é:', num_ale2[4])
print('O sexto valor é:', num_ale2[5])