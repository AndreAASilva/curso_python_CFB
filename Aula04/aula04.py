#Tipos simples
x=1 #int
x="CFB Cursos" #string
x=15.6 #float
x=False #bool

n1=5;n2=2;x=complex(n1,n2)

#list (Array)

x=["Carro", "Avião", "Navio"] #list / Array
#Modificando o item da lista
x[0] = "André"

#Tupla
x = ("Carro", "Avião", "Navio") #A tupla diferente do Array ou list não pode ter seus itens alterados

x=range(0,100,1) #List

#Dictionary
x={
    "Canal": "CFB Cursos",
    "Curso": "Curso de Python",
    "Nome": "André"
    
}

#SET não repete os valores quando é chamado para ser impresso
x={5,7,4,5,4,8} #set

x=frozenset({5,7,4,5,4,8}) #frozenset congela os valores - Aprofundar na pesquisa para entender melhor


#Para imprimir i item da lista devemos informar a posição
#print("Valor: " + x[0])
#print('Valor do dictionary:' + x["Canal"])
print('Valor: '+ str(x))
print('Tipo da variável: '+ str(type(x)))

print(x)


