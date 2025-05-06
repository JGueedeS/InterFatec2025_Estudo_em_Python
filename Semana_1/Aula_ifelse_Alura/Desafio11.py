ano = int(input("Digite a sua data de nascimento: "))
alistamento = (ano - 2025) * -1
if(alistamento == 18):
    print("Você vai ser alistado esse ano")
elif(alistamento > 18):
    novo_ano = (alistamento - 18) * -1
    print("Você já foi alistado ha {} anos".format(novo_ano))
else:
    novo_ano = (alistamento - 18) * -1
    print("Você não tem idade para se alistar, faltam {} anos".format(novo_ano))