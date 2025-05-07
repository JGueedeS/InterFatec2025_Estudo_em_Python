sexos = ["F", "M"]
while True:
    usuario = input("Digite seu sexo (F/M): ").strip().upper()[0]
    for sexo in sexos:
        if usuario == sexo:
            print("Valor correto")
            exit()  
    print("Valor incorreto. Tente novamente.")
