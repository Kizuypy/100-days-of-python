# NÍVEL MÉDIO 🟡
# EXERCÍCIO 5: Analisador de Texto com Estatísticas
# Contexto: Análise de texto é comum em empresas (comentários, reviews, etc).
# Tarefa: Crie um programa que:

# 1. Peça várias frases ao usuário (loop - "adicionar outra frase?")
#    - Armazene todas as frases em uma lista

# 2. Para cada frase, conte e mostre:
#    - Quantidade de vogais (a, e, i, o, u)
#    - Quantidade de consoantes
#    - Total de caracteres (sem contar espaços)

# 3. No final, mostre um resumo geral:
#    - Total de frases analisadas
#    - Frase com mais vogais
#    - Frase com mais consoantes





frases = []
vogais = 'aeiouAEIOU'


while True:

    while True:
        pedir_frase = input("Digite sua frase: ").strip()
        
        if not pedir_frase:
            print("Frase não pode estar vazia!")
        else:
            frases.append(pedir_frase)
            print("Lista atual:", frases)
            break

    continuar = input("Deseja adicionar outra frase? (s/n): ").strip().lower()
    if continuar != "s":
        break


print("\n===== RESULTADO =====")


maior_vogais = 0
frase_mais_vogais = ""

maior_consoantes = 0
frase_mais_consoantes = ""


for frase in frases:
    contador_vogais = 0
    contador_consoantes = 0
    total_caracteres = 0

    for letra in frase:
        if letra == " ":
            continue

        total_caracteres += 1

        if letra in vogais:
            contador_vogais += 1
        elif letra.isalpha():
            contador_consoantes += 1

    
    if contador_vogais > maior_vogais:
        maior_vogais = contador_vogais
        frase_mais_vogais = frase

    if contador_consoantes > maior_consoantes:
        maior_consoantes = contador_consoantes
        frase_mais_consoantes = frase


    print("\nFrase:", frase)
    print("Vogais:", contador_vogais)
    print("Consoantes:", contador_consoantes)
    print("Total de caracteres (sem espaço):", total_caracteres)



print("\n===== RESUMO GERAL =====")
print("Total de frases analisadas:", len(frases))
print("Frase com mais vogais:", frase_mais_vogais)
print("Frase com mais consoantes:", frase_mais_consoantes)