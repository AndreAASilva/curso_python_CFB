#Booleam - True ou False

aula = "André Anderson"
aula02 = ""

#Aqui ele está verificando se há um conteúdo dentro da string, com há, é True
print(bool(aula))

#Aqui verifica que a string é vazia e com isso gera um False
print(bool(aula02))

if aula:
    print('Possui texto')
else:
    print('Vazio')
    
#Qualquer valor diferente de zero é True

numero = 0

print(bool(numero))

