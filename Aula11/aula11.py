# Aula de IF, ELIF e ELSE

a = 10
b = 5
res = 0
op = '9'

dinheiro = 500
clima = "sol"
lugar = ""

if clima == "sol" and dinheiro >= 300 and dinheiro <= 500:
    lugar = "clube"
else:
    lugar = "cinema"

print('Vou ao '+ lugar)

#AND - 
# V V = V
# V F = F
# F V = F
# F F = F

#OR
# V V = V
# V F = V
# F V = V
# F F = F


"""
if op == "+":
    res=a+b

elif op == "-":
    res=a-b

elif op == "*":
    res=a*b

elif op == "/":
    res=a/b

else: 
    print("Operador Inválido")

print(str(a) + op + str(b) + " = " + str(res))

"""
