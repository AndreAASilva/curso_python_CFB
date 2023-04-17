import os

os.system('cls')


pal = 'Palmeiras'
fla = 'Flamengo'
cor = 'Corinthians'

pt_pal = int(input('Digite os pontos ganhos: '))
pt_fla = int(input('Digite os pontos ganhos: '))
pt_cor = int(input('Digite os pontos ganhos: '))

if pt_pal > pt_fla and pt_pal > pt_cor:
    print(f'O {pal} é o líder com {pt_pal}')
elif pt_fla > pt_pal and pt_fla > pt_cor:
    print(f'O {fla} é o líder com {pt_fla}')
else:
    print(f'O {cor} é o líder com {pt_cor}')
    
pontuacao = [pt_pal, pt_fla, pt_cor]
pontuacao.sort(reverse=False)

print(pontuacao[0], pontuacao[1], pontuacao[2])        
    

#print('O {} tem {} pontos'. format(pal, pt_pal))
#print('O {} tem {} pontos'. format(fla, pt_fla))
#print('O {} tem {} pontos'. format(cor, pt_cor))

