frase = ("Estudando para interfatec")
frase2 = ("  Testeando ")
#Cortar a frase: [3:] = onde inicia o corte => vai iniciar na 3 casa
#Cortar a frase: [:3] = onde termina o corte => vai finalizar na 3 casa
#Cortar a frase: [3:3:2] = criterio de corte => vai pular 2 casas
#Quando deixa vazio significa que inicia o processo da 1 casa ou vai até o final
print(frase[3:])
print('''Lorem Ipsum is simply dummy text of the printing and 
typesetting industry. Lorem Ipsum has been 
the industry''') #Colocar um texto em varias linhas
print(frase.count("a")) #contar a quantidade de caracter
print(len(frase)) #comprimento da frase
print(frase.find("o")) #procurar a palavra ou frase
print(frase.replace('interfatec', 'curso')) #reescrever a palavra
print(frase.upper()) #deixar em maisculo
print(frase.lower()) #deixar em minusculo
print(frase.capitalize()) #Deixar a primeira letra em maisculo
print(frase.title()) #Deixar maisculo toda letra com espaco
print(frase2.strip()) #remover espacos inuteis
print(frase2.lstrip()) #remover espacos inuteis da esquerda
print(frase2.rstrip()) #remover espacos inuteis da direita
print(frase.split()) #Dividir em lista
print('-'.join(frase)) #colocar a palavra em aspas