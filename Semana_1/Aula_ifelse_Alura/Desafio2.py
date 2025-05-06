dia1 = int(input("Iforme os dias para a atividade A: "))
dia2 = int(input("Iforme os dias para a atividade B: "))
dia3 = int(input("Iforme os dias para a atividade C: "))



if(dia1 < 0 or dia2 < 0 or dia3 < 0):
    soma = dia1+dia2+dia3
    print("Erro os dias digitados foram negativos")
else:
    print("A soma dos seus dias foram: {}".format(soma))