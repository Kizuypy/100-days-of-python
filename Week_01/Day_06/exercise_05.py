# 🧡 Exercício 5: Filtrar Alunos Aprovados com Dict Comprehension
# Descrição:
# Dado um dicionário de alunos e notas, crie um novo dicionário apenas com alunos aprovados (nota >= 7).
# Requisitos:

# Dicionário: {"Ana": 8.5, "João": 6.0, "Maria": 9.0, "Pedro": 5.5, "Carla": 7.5}
# Use dict comprehension com if
# Filtre apenas nota >= 7



alunos =  {"Ana": 8.5, "João": 6.0, "Maria": 9.0, "Pedro": 5.5, "Carla": 7.5}

aprovado = {aluno: nota for aluno, nota in alunos.items() if nota >= 7}
print(aprovado)

