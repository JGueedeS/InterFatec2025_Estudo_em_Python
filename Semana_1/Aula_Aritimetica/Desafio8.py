import math
Numero = int(input('Digite um número do angulo: '))
seno = math.sin(math.radians(Numero))
cosseno = math.cos(math.radians(Numero))
print('O angulo ({}), com o seno de {:.2f} e o cosseno de {:.2f} '.format(Numero, seno, cosseno))