Produto = str(input('Qual produto: '))
Valor = float(input('Qual o valor: '))
Desconto = (Valor * 0.05)
Valor_final = Valor - Desconto
print('O seu produto ({}) do valor de {} tem o desconto de 5% e com valor final de {}'.format(Produto, Valor, Valor_final))