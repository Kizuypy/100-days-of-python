# NÍVEL MÉDIO 🟡
# EXERCÍCIO 4: Sistema de Aprovação de Candidatos com Múltiplas Vagas
# Contexto: RH precisa filtrar candidatos por critérios.
# Tarefa: Crie um programa que:

# 1. Permita avaliar vários candidatos (loop com "avaliar outro?")

# 2. Para cada candidato, peça:
#    - Nome do candidato
#    - Idade (deve estar entre 18 e 65 anos)
#    - Anos de experiência (não pode ser negativo)
#    - Conhece Python? (sim/não)

# 3. Regras de aprovação (igual ao fácil):
#    - Idade entre 18 e 65 anos
#    - Pelo menos 2 anos de experiência OU conhece Python

# 4. Armazene os candidatos em uma lista

# 5. Mostre para cada um:
#    "Candidato [NOME]: APROVADO ✓" ou "Candidato [NOME]: REPROVADO ✗"
#    E o motivo da reprovação (se houver)

# 6. No final, mostre um resumo:
#    - Total de candidatos avaliados
#    - Quantos foram aprovados
#    - Quantos foram reprovados

# Validações básicas:
#    - Idade e experiência devem ser números válidos
#    - Se errar, pedir novamente




candidatos = []

while True:

 
    while True:
        nome = input("Digite o nome do candidato: ").strip()
        if nome:
            break
        print("Nome não pode ser vazio!")

   
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if 18 <= idade <= 65:
                break
            print("Idade deve estar entre 18 e 65 anos!")
        except ValueError:
            print("Digite um número válido!")

    
    while True:
        try:
            experiencia = int(input("Digite os anos de experiência: "))
            if experiencia >= 0:
                break
            print("Experiência não pode ser negativa!")
        except ValueError:
            print("Digite um número válido!")

    
    while True:
        conhece_python = input("Conhece Python? (sim/não): ").strip().lower()
        if conhece_python in ["sim", "não"]:
            break
        print("Digite apenas 'sim' ou 'não'!")

    
    motivo = ""

    if experiencia >= 2 or conhece_python == "sim":
        aprovado = True
    else:
        aprovado = False
        motivo = "Menos de 2 anos de experiência e não conhece Python"

    
    candidatos.append([nome, idade, experiencia, conhece_python, aprovado, motivo])

    print("Candidato cadastrado com sucesso!")

    continuar = input("Deseja cadastrar outro candidato? (s/n): ").strip().lower()
    if continuar != "s":
        break




print("\n===== RESULTADO FINAL =====")

total_aprovados = 0
total_reprovados = 0

for candidato in candidatos:
    nome = candidato[0]
    aprovado = candidato[4]
    motivo = candidato[5]

    if aprovado:
        print(f"Candidato {nome}: APROVADO ✓")
        total_aprovados += 1
    else:
        print(f"Candidato {nome}: REPROVADO ✗")
        print(f"Motivo: {motivo}")
        total_reprovados += 1

print("\n===== RESUMO =====")
print(f"Total avaliados: {len(candidatos)}")
print(f"Aprovados: {total_aprovados}")
print(f"Reprovados: {total_reprovados}")