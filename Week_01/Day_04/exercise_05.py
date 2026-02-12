# ❤️ DIFÍCIL: Sistema de Votação com Ranking
# Contexto: Sistemas de votação precisam contar votos e mostrar resultados ordenados.
# Tarefa: Crie um programa que:

# Tenha uma lista de candidatos: ['Ana', 'João', 'Maria', 'Pedro']
# Simule 10 votos aleatórios (pode pedir pro usuário ou usar número de 0 a 3)
# Conte os votos em um dicionário
# Mostre o ranking do mais votado para o menos votado
# Mostre quem ganhou a eleição

# Requisitos extras:

# Use um dicionário para contar votos
# Use .items() para pegar pares chave-valor
# Para ordenar, você pode:

# Criar uma lista de tuplas (candidato, votos)
# Ordenar manualmente comparando os valores (sem usar sorted())


candidatos = ['Ana', 'João', 'Maria', 'Pedro']

# Dicionário de votos (já iniciando com 0)
votos = {
    'Ana': 0,
    'João': 0,
    'Maria': 0,
    'Pedro': 0
}

# Sistema para votação

for i in range(10):
    print(f"\nVotação {i+1}")
    print("Cadidatos disponíveis:", candidatos)

    votar_candidato = input("Digite o nome do candidato: ")

    if votar_candidato in candidatos:
        votos[votar_candidato] += 1
    else:
        print("Candidato inválido! Voto não contabilizado!")


print("\n📊 RESULTADO FINAL")
for candidato, total in votos.items():
    print(f"{candidato}: {total} votos")

ranking = list(votos.items())
    

for i in range(len(ranking)):
    for j in range(len(ranking)- 1):
        if ranking[j][1] < ranking[j + 1][1]:
            ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]
print("\n Ranking Final")

for posicao, (candidato, total) in enumerate(ranking, start=1):
    print(f"{posicao}º Lugar: {candidato} com {total} votos")


print(f"\n🎉 O vencedor foi: {ranking[0][0]}!")