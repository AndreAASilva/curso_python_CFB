num1 = num2 = res = 0

#Escopo global e local

def cn():
    canal = "CFB Cursos"
    print(canal)

cn()

def cn2():
    #EU posso escrever uma variável global dentro da função e declarar ela como global escrevendo o global e em seguida o nome da variável, abaixo repetindo a variável e sua informação. Ou podemos escrever ela fora da função para ter o mesmo efeito.
    global canal2 
    canal2 = "Curso de Python"
    
cn2()

print(canal2)

canal3 = "Apenas para teste"

def teste():
    print(canal3)

teste()

canal4 = 'Novo teste'

def teste2():
    print('Eu estou imprimindo minha variável: '+ canal4)

teste2()