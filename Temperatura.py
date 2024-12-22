def Temperatura():
    while True:
        Valor = input('Digite a temperatura em Celsius para saber a temperatura em Fahrenheit e Kelvin (ou digite "sair" para encerrar o programa): ')
        if Valor.lower() == 'sair':
            break
        try:
            Fahrenheit = float(Valor) * 1.8 + 32
        except ValueError:
            print('Digite apenas números(ou digite "sair" para encerrar o programa): ')
            continue
        print(f'{Valor}°C é igual a {Fahrenheit}°F')

    print('Programa encerrado. Obrigado por usar o nosso programa.')
    
Temperatura()