velocidade = int(input("Digite a velocidade do seu carro:"))
if(velocidade > 80):
    multa = (velocidade - 80) * 7
    print("Velocidade acima do permitido (80 KM), valor a ser multado de {}".format(multa))
else:
    print("Velocidade dentro das conformidades")