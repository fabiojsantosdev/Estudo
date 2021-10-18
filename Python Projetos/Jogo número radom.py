import random

numero_aleatorio = random.randint(1,10)
acertou = False

print('=====Adivinhe número de 1 a 10.=====')


while acertou == False:
    chute = int(input('Informe numero inteiro entre 1 a 10:  '))
    if chute > numero_aleatorio:
     
        print('====Chute maior que valor gerado.====')

    elif chute < numero_aleatorio:
        
        print('====Chute foi menor que valor gerado.====')
        

    elif chute == numero_aleatorio:
        
        acertou = True
        print('====Parabéns você acertou.====')



