nomes = []
while True:
    nome = str(input("Digite seu nome ou saia:"))
    if nome != "sair":
        nomes.append(nome)
        continue
    else:
        print(nomes)
        break