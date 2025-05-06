Viagem = int(input("Qual a distancia da sua viagem: "))
if(Viagem <= 200):
    preco1 = Viagem * 0.50
    print("O preco da sua viagem ficou R$ {} calculando R$ 0.50 por KM".format(preco1))
else:
    preco2 = Viagem * 0.45
    print("O preco da sua viagem ficou {} calculando R$ 0.45 por KM".format(preco2))