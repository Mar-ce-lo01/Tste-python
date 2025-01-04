import math

def geometria():
    while True:
       Ângulo = input('Digite o ângulo para saber o seno, cosseno e tangente(ou digite "sair" para encerrar o programa): ')
       if Ângulo.lower() == 'sair':
           break
       try:
           Ângulo = int(Ângulo)
           Ângulo = math.radians(Ângulo)
       except ValueError:
           print('Coloque só nemeros nada de letra')
           continue
       Seno = math.sin(Ângulo)
       Cosseno = math.cos(Ângulo)
       Tangente = math.tan(Ângulo)
       print(f'O seno  é {Seno:.2f}, o cosseno  é {Cosseno:.2f} e a tangente  é {Tangente:.2f}')
    print("Obrigado por usar o nosso programar")
geometria()