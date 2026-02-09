# NÍVEL MÉDIO 🟡
# EXERCÍCIO 10: Jogo de Adivinhação com Níveis de Dificuldade
# Contexto: Gamificação é usada em treinamentos corporativos.
# Tarefa: Crie um jogo onde:

# 1. No início, pergunte o nível de dificuldade:
#    - Fácil: 1 a 50 (10 tentativas)
#    - Médio: 1 a 100 (7 tentativas)
#    - Difícil: 1 a 200 (5 tentativas)

# 2. O jogo funciona igual ao fácil:
#    - Sorteia número baseado no nível escolhido
#    - Usuário tenta adivinhar
#    - Diz "maior" ou "menor"
#    - Limite de tentativas conforme dificuldade

# 3. No final mostre:
#    - Se ganhou ou perdeu
#    - Quantas tentativas usou
#    - Pergunte: "Jogar novamente? (s/n)"


import random

while True:
    print("\n=== Jogo de Adivinhação ===")
    
    nivel = input("Escolha o nível (fácil, médio, difícil): ").strip().lower()
    
    if nivel == "fácil":
        limite = 50
        tentativas_max = 10
    elif nivel == "médio":
        limite = 100
        tentativas_max = 7
    elif nivel == "difícil":
        limite = 200
        tentativas_max = 5
    else:
        print("Nível inválido! Digite fácil, médio ou difícil.")
        continue

    numero_secreto = random.randint(1, limite)
    tentativas = 0
    ganhou = False

    print(f"\nTente adivinhar o número entre 1 e {limite}. Você tem {tentativas_max} tentativas!")

    while tentativas < tentativas_max:
        try:
            chute = int(input(f"Tentativa {tentativas + 1}/{tentativas_max}: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        tentativas += 1

        if chute == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            ganhou = True
            break
        elif chute < numero_secreto:
            print("O número é maior!")
        else:
            print("O número é menor!")

    if not ganhou:
        print(f"Fim de jogo! O número era {numero_secreto}.")

    jogar_novamente = input("Jogar novamente? (s/n): ").strip().lower()
    if jogar_novamente != "s":
        print("Obrigado por jogar! Até mais!")
        break
