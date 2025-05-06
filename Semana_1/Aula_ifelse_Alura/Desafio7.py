nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda note: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3)/3

if(media < 5):
    print("Média: {:.2f}".format(media))
    print("Reprovado")
elif  5 <= media < 7:
    print("Média: {:.2f}".format(media))
    print("Recuperação")
else:
    print("Média: {:.2f}".format(media))
    print("Aprovado")