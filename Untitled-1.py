def Calculadora():
    while True:
        try:
            Valor1 = int(input('Digite algum número: '))
            Valor2 = int(input('Digite um segundo número: '))

            Soma = Valor1 + Valor2
            Subrtação = Valor1 - Valor2
            Multiplicação = Valor1 * Valor2
            Divisão = Valor1/Valor2

            print(f'A soma de {Valor1} + {Valor2} = {Soma}  a divisão é {Divisão} a multiplicação do produto é {Multiplicação} e a subtração é {Subrtação}')
            
            continuar = input('Deseja fazer outra soma? (s/n): ').strip().lower()
            if continuar != 's':
                break
        except ValueError:
            print('Digite apenas números inteiros')

Calculadora()
