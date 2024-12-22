def Pintores():
    while True:
        Altura = input("coloque a largura ou a altura de uma parede em metros, calcule a sua Área e a quantidade de tinta necessária para pintá-la(ou didite 'sair' para encerra p programa.):")
        if Altura.lower() == 'sair':
            break

        Largura = input("Digite a largura ou altura(ou dite 'sair' para encerrar o programar): ")
        if Largura.lower() == 'sair' :
            break

        try:
            Altura = float(Altura)
            Largura = float(Largura)
        except ValueError:
            print('digite apenas números nada mais (ou digite "sair" para encerrar o programar): ')
            continue
        Área = Largura * Altura
        Litros = Área / 2
        Litros_formatado = f"{Litros:.2f}"

        print(f'A quantidade de tinta necessaria para pintar á parede é {Litros} e a Área da parede é {Área} m^2')
    print("Programa encerrado. Obrigado por usar o nosso programar de pinturas.")

Pintores()   