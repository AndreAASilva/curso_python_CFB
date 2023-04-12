#Aula 02 de string

curso = "Curso de Python"

# IN e NOT IN verifica se a palavra está na string

res_in = "Curso" in curso
print(res_in)

res_not = "Curso" not in curso
print(res_not)

# O IN e NOT IN encontram a palavra da forma que ela foi escrita, caso haja alguma letra diferente como maiúcula e minúscula não será localizada, para corrigir esta falha uma das opções foi a utlização do upper() onde vai converter as palavras em maiúculo e corrigir a busca

#Exemplo criando uma variável da palvra, porém podemos escrever a palavra diretamente sem a necessidade de criar uma variável
palavra = "Curso"

res_mai = "CuRso".upper() in curso.upper()
print(res_mai)

res_teste = palavra in curso

if(res_teste):
    print('Encontrei a palavra: {}'.format(palavra))
else:
    print('Não localizei a palavra: {}'.format(palavra))


cidade = "São Paulo"
dia = 12
mes = "Abril"
ano = 2023
canal = 'CFB Cursos'

#Aqui vão alguns exemplos de caracteres de escapes com a utlização da barra invertida
data = '{}, {} de {} de {}\n\"{}\"'

print(cidade,', ',dia," de ", mes,' de ', ano)

#Concatenando convertendo para string
print(cidade + ', ' + str(dia) + ' de ' + mes + ' de ' + str(ano))
 
#Utilizando o format
print(data.format(cidade, dia, mes, ano, canal))

"""
\'
\""
\n - Quebra de linha
\r - Retorno
\t - Tabulação
\b - backspace

Há outros para trabalhar com string

"""

