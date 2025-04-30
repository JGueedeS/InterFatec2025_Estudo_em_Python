peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em CM: "))

imc = peso / (altura ** 2)


if(imc < 18.5):
    print("Você está abaixo do peso")
    print("Seu IMC é de {:.2f}".format(imc))
elif(imc < 25):
    print("Seu IMC é de {:.2f}".format(imc))
    print("Você está acima do peso")
else:
    print("Seu IMC é de {:.2f}".format(imc))
    print("Você está com peso normal")
