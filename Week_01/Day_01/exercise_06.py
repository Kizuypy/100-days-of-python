# NÍVEL MÉDIO 🟡
# EXERCÍCIO 6: Lista de Tarefas (To-Do List Simples)
# Contexto: Gestão de tarefas é essencial em qualquer empresa.
# Tarefa: Crie um programa com menu:

# Adicionar tarefa
# Listar tarefas
# Sair

# Use while para manter o programa rodando até o usuário escolher sair.
# Dicas:

# Use uma lista vazia: tarefas = []
# Use append() para adicionar
# Use for para listar
# Use break para sair do while



tarefas = []

while True:
    print('\n1 - Adicionar tarefa')
    print('2 - Listar tarefas')
    print('3 - Sair')

    opcao = input('Escolha uma opção: ')


    if opcao == '1':
        adicionar_tarefa = input('Adicione uma tarefa: ')
        tarefas.append(adicionar_tarefa)

    elif opcao == '2':
        if len(tarefas) == 0:
            print('Nenhuma Tarefa cadastrada')
        else:
            print('\nLista de Tarefas: ')
            for tarefa in tarefas:
                print('-', tarefa)
  
    elif opcao == '3':
        print('Saindo...')
        break
    else:
        print('Opção Inválida.')