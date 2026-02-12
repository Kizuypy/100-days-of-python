# 💚 FÁCIL 1: Cadastro de Alunos
# Contexto: Escolas precisam armazenar dados de alunos.
# Tarefa: Crie um programa que:

# Tenha um dicionário vazio para armazenar alunos
# Peça ao usuário o nome do aluno
# Peça a nota do aluno
# Armazene no dicionário onde a chave é o nome e o valor é a nota
# Repita 3 vezes
# No final, mostre todos os alunos e suas notas

# Dica: Use um for com range(3) para repetir 3 vezes.


alunos = {}

for i in range(3):
    nome_aluno = input("Digite o nome do aluno: ").strip().title()
    try:
        nota_aluno = float(input("Digite a nota do aluno: "))
        alunos[nome_aluno] = nota_aluno
    except ValueError:
        print("Somente números!")
print(alunos)