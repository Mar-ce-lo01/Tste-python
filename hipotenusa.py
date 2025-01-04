import math

def hipotenusao():
    while True:
        cateto = input("Coloque o cateto oposto: ")
        if cateto.lower() == 'sair':
            break
        adjacent = input('Coloque o cateto adjacente: ')
        if adjacent.lower() == 'sair':
            break
        try:
            cateto = float(cateto)
            adjacent = float(adjacent)  
        except ValueError:
            print('Coloque só números reais')
            continue
        hipotenusa = math.sqrt(cateto ** 2 + adjacent ** 2)
        hipotenusa2 = int(hipotenusa)

        print(f'A hipotenusa é {hipotenusa2} ')
    
    print('Obrigado por usar o nosso programa')

hipotenusao()