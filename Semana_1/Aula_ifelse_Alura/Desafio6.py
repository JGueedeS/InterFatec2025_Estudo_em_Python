from datetime import datetime

user = str(input("Qual seu nome: "))
hora_atual = datetime.now()
hora = hora_atual.hour
if 8 <= hora <= 18:
    print("Bem vindo, SR(a) {}".format(user))
else:
    print("Fora do horario de trabalhon, SR(a) {}".format(user))