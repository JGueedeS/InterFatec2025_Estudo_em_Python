'''idade = 22 #variavel global
def minha_funcao():
    nome = "Jeff" #variavel local
    print("Esse é meu nome {} e minha idade {}".format(nome, idade))

minha_funcao()'''

'''def somar(n1, n2): #parametros
    resultado = n1 + n2
    print("A soma de {} + {} é {}".format(n1, n2, resultado))

somar(6, 10) #Argumentos'''

def somar(n1, n2): #parametros
    resultado = n1 + n2
    return resultado

resultado_soma =somar(6, 10)
print(resultado_soma)