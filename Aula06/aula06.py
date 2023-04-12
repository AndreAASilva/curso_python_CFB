#Strings PT01

curso = "Curso de Python"

#Imprimindo um determinado valor
print(curso[10])

#Imprimindo os valores solicitados de um ponto a outro
print(curso[0:5])
print(curso[6:8])
print(curso[9:15])

#Imprimindo o tamanho da string
print('Tamanho do texto: ' + str(len(curso)))

#Método strip() remove espaços da string
curso02 = " Curso de Python com espaços dos lados "

print(curso02.strip())
print('O tamanho da string utilizando o strip() é:', len(curso02))

#lower() converte letras maiúsculas em minúsculas 
curso_min = 'CURSO DE PYTHON MINÚSCULO'

print(curso_min.lower())

#upper() converte letras minúsculas em maiúsculas
curso_mai = 'curso de python maiúsculo'

print(curso_mai.upper())


#replace() altera valores da srting

curso_alt = 'Curso de Python modificando valores da string'

print(curso_alt.replace('Python', 'MODIFICADO'))

#split() divide a string onde determinarmos o valor da divisão dentro dos parenteses

curso_div = "Curso de Python utilizando o método split"

#Após definir o local da divisão, podemos solicitar a impressão, pois o split() transformou a string num Array
curso_spl = curso_div.split('i')
print(curso_spl[1])