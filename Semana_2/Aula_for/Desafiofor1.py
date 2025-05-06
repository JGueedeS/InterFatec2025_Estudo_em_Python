import time
iniciar = int(input("Digite 1 par iniciar a contagem regressiva: "))
if(iniciar == 1):
    for contagem in range(0, 11):
        print(contagem)
        time.sleep(1)
print("🎆")
