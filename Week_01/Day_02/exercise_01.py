# NÍVEL MÉDIO 🟡
# EXERCÍCIO 1: Sistema de Cadastro de Funcionários
# Contexto: Toda empresa precisa cadastrar funcionários no sistema.
# Tarefa: Crie um programa que:

# 1. Mostre um menu com opções:
#    - Cadastrar funcionário
#    - Listar todos os funcionários
#    - Mostrar relatório geral
#    - Sair do programa

# 2. No cadastro, peça:
#    - Nome do funcionário (não pode ser vazio ou só números)
#    - Idade (deve estar entre 18 e 70 anos)
#    - Salário (deve ser maior que zero)

# 3. Faça validações:
#    - Se algum dado estiver errado, mostre mensagem e peça novamente
#    - Só aceite dados válidos

# 4. Calcule automaticamente:
#    - Desconto de INSS: 8% do salário bruto
#    - Salário líquido: salário bruto - INSS

# 5. Após cadastrar, mostre os dados formatados:
#    "Funcionário [NOME], [IDADE] anos"
#    "Salário Bruto: R$ [VALOR]"
#    "Desconto INSS: R$ [VALOR]"
#    "Salário Líquido: R$ [VALOR]"

# 6. Permita cadastrar vários funcionários (armazene em uma lista)

# 7. Na opção "Listar", mostre todos os funcionários cadastrados

# 8. Na opção "Relatório", mostre:
#    - Total de funcionários cadastrados
#    - Média salarial (salário bruto)
#    - Nome do funcionário com maior salário

# 9. O programa só deve encerrar quando o usuário escolher "Sair"


funcionarios = []
desconto_inss = 8
total_salarios = 0

### Menu de opções:



while True:
    print('\n=== SISTEMA DE CADASTRO ===')
    print('1 - Cadastrar funcionário')
    print('2 - Listar todos os funcionários')
    print('3 - Mostrar relatório geral')
    print('4 - Sair do programa')


    opcao = input('Escolha uma das opções: ')

# 2. No cadastro, peça:
#    - Nome do funcionário (não pode ser vazio ou só números)
#    - Idade (deve estar entre 18 e 70 anos)
#    - Salário (deve ser maior que zero)



    if opcao == '1':
    # Validação do NOME (fica pedindo até ser válido)
        while True:
            nome_funcionario = input('Digite o nome do funcionário: ')
            
            if nome_funcionario.strip() == '':
                print('❌ Nome não pode ser vazio! Tente novamente.')
                continue  # Volta pro início deste while
            
            if nome_funcionario.isdigit():
                print('❌ Nome não pode ser apenas números! Tente novamente.')
                continue
            
            break  # Sai do loop se o nome for válido
        
        
        # Validação da IDADE (fica pedindo até ser válida)
        while True:
            try:
                idade_funcionario = int(input('Digite a idade do funcionário: '))
                
                if not 18 <= idade_funcionario <= 70:
                    print('❌ Idade deve estar entre 18 e 70 anos! Tente novamente.')
                    continue
                
                break  # Sai do loop se a idade for válida
                
            except ValueError:
                print('❌ Idade deve ser um número inteiro! Tente novamente.')
        
        
        # Validação do SALÁRIO (fica pedindo até ser válido)
        # 5. Após cadastrar, mostre os dados formatados:
#       "Funcionário [NOME], [IDADE] anos"
#       "Salário Bruto: R$ [VALOR]"
#       "Desconto INSS: R$ [VALOR]"
#       "Salário Líquido: R$ [VALOR]"
        while True:
            try:
                salario_bruto = float(input('Digite o salário do funcionário: '))
                calculo_desconto = salario_bruto * (desconto_inss / 100)
                salario_liquido = salario_bruto - calculo_desconto
                if salario_bruto <= 0:
                    print('❌ Salário deve ser maior que zero! Tente novamente.')
                    continue
                
                break  # Sai do loop se o salário for válido
                
            except ValueError:
                print('❌ Salário deve ser um número válido! Tente novamente.')
        
        
        # Agora que TODOS os dados estão válidos, adiciona na lista
        funcionario = [nome_funcionario, idade_funcionario, salario_bruto, calculo_desconto, salario_liquido]
        funcionarios.append(funcionario)
        print('✅ Funcionário cadastrado com sucesso!')
    
    elif opcao == '2':
        if len(funcionarios) == 0:
            print('Nenhum funcionário cadastrado!')
        else:
            print('\nLista de funcionários: ')
            for funcionario in funcionarios:
                print(f'Nome: {funcionario[0]}')
                print(f'Idade: {funcionario[1]}')
                print(f'Salário Bruto: {funcionario[2]:.2f}')
                print(f'Desconto INSS: {funcionario[3]:.2f}')
                print(f'Salário Liquido: {funcionario[4]:.2f}')
                print('-' * 20)


# 8. Na opção "Relatório", mostre:
#    - Total de funcionários cadastrados
#    - Média salarial (salário bruto)
#    - Nome do funcionário com maior salário


    elif opcao == '3':
        if len(funcionarios) == 0:
            print('Nenhum funcionário cadastrado')
        else:
            print('\n=== RELATÓRIO GERAL ===')
            total_funcionarios = len(funcionarios)
            total_salarios = 0

            for funcionario in funcionarios:
                total_salarios += funcionario[2]

            media_salarial = total_salarios / total_funcionarios

            # Funcionário com maior salário

            maior_salario = funcionarios[0]

            for funcionario in funcionarios:
                if funcionario[2] > maior_salario[2]:
                    maior_salario = funcionario

            print(f'Total de funcionários: {total_funcionarios}')
            print(f'Média salarial: {media_salarial:.2f}')
            print(f'O maior salário: {maior_salario[0]} - R$ {maior_salario[2]:.2f}')
    elif opcao == '4':
        print('Saindo do programa...')
        exit()