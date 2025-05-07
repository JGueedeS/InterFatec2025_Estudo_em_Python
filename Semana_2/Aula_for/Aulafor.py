'''for c in range(1, 5):
    print("Testando laço")
print("FIM")'''
inicio = int(input("Digite o inicio: "))
passo = int(input("Digite o passo: "))
fim = int(input("Digite o fim: "))
for c in range(inicio, fim+1, passo):
    print(c)
