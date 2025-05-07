maca = int(input("Digite a quantidade maçãs vendidas: "))
banana = int(input("Digite a quantidade de bananas vendidas: "))

if(maca > banana):
    print("As maçãs foram mais vendidas que as bananas")
elif(banana > maca):
    print("As bananas foram mais vendidas que as maçã")
else:
    print("As vendas foram iguais")