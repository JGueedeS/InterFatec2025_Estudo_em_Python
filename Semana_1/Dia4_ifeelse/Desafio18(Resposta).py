from random import randint
Numero = int(input("Digite um numero entre 0 e 5:"))
sorteio = randint(0, 5)

if(Numero == sorteio):
    print("Pensando...")
    print("vocë acertou o numero que eu estava pensando ({})".format(sorteio))
else:
    print("Número errado, tente de novo. Numero que eu pensei {}".format(sorteio))