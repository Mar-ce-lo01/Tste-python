def Desconto():
    while True:
        Desconto = input('Uma loja teve 5% de desconto em todos os seus produtos coloque preço de todaas as suas comprar para ver seu desconto final(ou digite "sair" para encerrar o programar.): ')
        if Desconto.lower() == "sair":
            break
        try:
            Desconto = float(Desconto)
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        Porcentagem = Desconto * 0.05
        Preço_final = Desconto - Porcentagem
        Preço_final2 = f"{Desconto:.2f}"

        print(f"O seu desconte de {Desconto} é de {Preço_final}")
    print('Proframa encerrado. Obrigado por acessar a nosso programa da loja.')

Desconto()