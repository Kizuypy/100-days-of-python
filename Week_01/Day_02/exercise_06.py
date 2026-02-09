# NÍVEL MÉDIO 🟡
# EXERCÍCIO 6: Sistema de Tarefas com Prioridades
# Contexto: Gestão de tarefas é essencial em qualquer empresa.
# Tarefa: Crie um programa com menu:

# 1. Adicionar tarefa:
#    - Nome da tarefa (não pode ser vazio)
#    - Prioridade: Alta, Média ou Baixa
#    - Armazene como: [nome, prioridade]

# 2. Listar tarefas:
#    - Mostre todas numeradas com suas prioridades
#    - Exemplo: "1. Reunião com cliente [ALTA]"

# 3. Marcar tarefa como concluída:
#    - Peça o número da tarefa
#    - Remova ela da lista
#    - Mostre: "Tarefa '[NOME]' concluída! ✓"

# 4. Sair do programa
prioridades = ''
tarefas = []

while True: 

    print('\n Escolha uma das opções a baixo:')
    
    opcao = input('1 - Adicionar Tarefa\n'
    '2 - Listar Tarefas\n'
    '3 - Marcar tarefa como concluida\n'
    '4 - Sair do programa ').strip()
    if not opcao:
        print('Opção não pode estar vazia!')
        continue
    elif opcao == '1':
        while True:
            nome_tarefa = input('Digite o nome da tarefa: ').strip()
            if not nome_tarefa:
                print("A tarefa não pode estar vazia!")
            else:
                break
        while True:
            prioridade_tarefa = (input("Digite a prioridade da terefa: \n"
            "1 - Alta\n"
            "2 - Média\n"
            "3 - Baixa: "))
            
            if prioridade_tarefa == '1':
                prioridades = 'Alta'
                break
            elif prioridade_tarefa == '2':
                prioridades = 'Média'
                break
            elif prioridade_tarefa == '3':
                prioridades = 'Baixa'
                break
            else:
                 print("Opção inválida! Digite 1, 2 ou 3.")
        tarefas.append([nome_tarefa, prioridades])
        print("Lista atual:", tarefas)
    elif opcao == '2':
        if len(tarefas) == 0:
            print('Nenhuma tarefa registrada!')
        else:
            print('\n Lista de tarefas registradas:')
            for indice, tarefa in enumerate(tarefas, start=1):
                print(f"{indice}. {tarefa[0]} [{tarefa[1].upper()}]")

    elif opcao == '3':
        if len(tarefas) == 0:
            print('Não há tarefas para concluir!')
        else:
            print('\nEscolha o número de tarefa para concluir: ')

            for i, tarefa in enumerate(tarefas,start=1 ):
               print(f"{i}. {tarefa[0]} [{tarefa[1]}]")
            while True:
                try:
                    numero = int(input("Digite o número da tarefa: "))  
                    indice = numero - 1

                    if  0 <= indice < len(tarefas):
                        tarefa_removida = tarefas.pop(indice)
                        print(f"Tarefa '{tarefa_removida[0]}' concluída! ✓")
                        break
                    else:
                        print('Número inválido!')
                except ValueError:
                     print("Digite um número válido!")
    elif opcao == '4':
        print("Saindo do programa...")
        break
            
            



  

            




