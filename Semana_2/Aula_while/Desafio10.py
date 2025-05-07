multiplo = 1
numero = int(input("Digite um número: "))

while multiplo < 11:
    multiplicacao = numero * multiplo
    print("{} * {} = {}".format(numero, multiplo, multiplicacao))
    multiplo+=1
    