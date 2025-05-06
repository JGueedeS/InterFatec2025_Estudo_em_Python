velocidade = int(input("Digite sua velocidade em (KM): "))
if velocidade > 200:
    print("Valor do pedágio: R$ 30,00")
elif 100 < velocidade < 200:
    print("Valor do pedágio: R$ 20,00")
else:
    print("Valor do pedágio: R$ 10,00")