clima = input("Como está o clima hoje: ")
local = ''
valor = float(input("Quanto você tem: "))


if clima == "sol" and valor >= 300 and valor <= 500:
    local='clube'
elif clima  == 'chuva' and valor >= 300 and valor <= 500:
    local='clube' 
elif clima == "nublado" and valor >= 300 and valor <= 500:
    local='clube'
else: 
    local='cinema'
    
print('Você vai para o '+ local)