while True:
    Nota1 = input("Coloque sua primeira nota(ou escrevae 'sair' para encerrar o programar): ")
    if Nota1.lower() == 'sair':
        break
    
    Nota2 = input('Coloque sua segunda nota: ')
    Nota3 = input('Coloque sua terceira nota: ')
    Nota4 = input('Coloque sua quarta nota: ')

    try:
        n1 = float(Nota1)
        n2 = float(Nota2)
        n3 = float(Nota3)
        n4 = float(Nota4)
    except ValueError:
        print("Insira um numero válido ou escrevar'sair' para encerrar o programa.")
        continue

    soma_notas = n1 + n2 + n3 + n4
    media_final = soma_notas / 4
    print(f"A nota final é {media_final:.2f}")

print('programa encerrado. Obrigado po usar o nosso sistema.')