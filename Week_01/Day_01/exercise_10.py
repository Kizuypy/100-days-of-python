# NÍVEL MÉDIO 🟡
# EXERCÍCIO 10: Jogo de Adivinhação com Tentativas Limitadas
# Contexto: Gamificação é usada em treinamentos corporativos.
# Tarefa: Crie um jogo onde:

# O programa escolhe um número aleatório de 1 a 100
# O usuário tem 7 tentativas para adivinhar
# A cada tentativa, diga se o número é maior ou menor
# No final, mostre se ganhou ou perdeu e quantas tentativas usou

# Dicas:

# Use: from random import randint e numero = randint(1, 100)
# Use um contador de tentativas
# Use while com condição de tentativas <= 7
# Use if/elif para comparar

from random import randint

numero_secreto = randint(1,100)

tentativas =  1

while tentativas <= 7:
    chute = int(input(f'Tentativa {tentativas}/7 - Digite um número: '))

    if chute == numero_secreto:
        print('Você acertou!')
        break

    elif chute < numero_secreto:
        print('O número é maior')
    else: 
        print('O número é menor.')

    tentativas += 1

    
else:
    print('Você perdeu!')
    print(f'O número era {numero_secreto}')