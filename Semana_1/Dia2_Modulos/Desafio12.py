import random
Aluno1 = str(input('Primeiro aluno: '))
Aluno2 = str(input('Segundo aluno: '))
Aluno3 = str(input('Terceiro aluno: '))
Aluno4 = str(input('Quarto aluno: '))
Sorteio = random.choice([Aluno1, Aluno2, Aluno3, Aluno4])

print('O aluno sorteado foi o {} '.format(Sorteio))