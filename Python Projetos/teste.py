tentativa = 0
while (tentativa <3):
    try:
        
        n1 = int(input('Digite primeiro numero: '))
        n2 = int(input('Digite segundo numero: '))
        s  = n1 + n2
        m  = n1 * n2
        d  = n1 / n2
        di = n1 // n2
        e  = n1 ** n2
                
    except:
        
        print(f'Informe um numéro.')
        tentativa = tentativa +1     
    else: 
        
        print('A soma é {}, o produto é {} e a divisão e {:.2f}'.format(s,m,d))
        print('A divisão inteira é {} e a pontência {}'.format(di,e))
        tentativa = 3