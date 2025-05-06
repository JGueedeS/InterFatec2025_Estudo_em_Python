renda = int(input("Digite sua renda mensal: "))
parcela = int(input("Digite suas parcelas mensais: "))
calculo = parcela * (30 / 100)
if renda > 2000 and parcela < calculo:
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado: parcele acima da sua renda de 30%")