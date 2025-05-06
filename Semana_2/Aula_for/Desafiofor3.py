multiplicador = int(input("Digite seu multiplicador: "))
for contagem in range(0, 11):
    tabuada = contagem * multiplicador
    print("{} * {} = {}".format(contagem, multiplicador, tabuada))
