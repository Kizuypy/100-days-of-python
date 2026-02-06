# NÍVEL FÁCIL 💚
# EXERCÍCIO 4: Sistema de Aprovação de Candidatos
# Contexto: RH precisa filtrar candidatos por critérios.
# Tarefa: Crie um programa que peça:

# Idade do candidato
# Anos de experiência
# Conhece Python? (sim/não)

# Regras de aprovação:

# Idade entre 18 e 65 anos
# Pelo menos 2 anos de experiência OU conhece Python

# Mostre se o candidato foi aprovado ou reprovado e o motivo.
# Dicas:

# Use and, or para combinar condições
# Use >= e <= para faixas
# .lower() ajuda a aceitar "Sim", "SIM", "sim"

nome = input('Digite seu nome: \n')
idade = int(input('Digite sua idade: \n'))
anos_experiencia = int(input('Digite seus anos de experiência: \n'))
conhe_python = input('Conhece Python? [s/n]: ').lower()

if idade < 18 or idade > 65:
    print('Candidato reprovado por idade fora do permitido.')
elif anos_experiencia >= 2 or conhe_python == 's':
    print('Candidato aprovado!')
else:
    print('Candidato reprovado por falta de experiência ou conhecimento em Python.')