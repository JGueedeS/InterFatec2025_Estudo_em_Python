frase = str(input("digite uma frase: "))
print("A letra A aparece {} na frase".format(frase.count("a")))
print("A primeira letra A apareceu na posicao {}".format(frase.find("a")+1))
print("A ultima letra A apareceu na posicao {}".format(frase.rfind("a")+1))