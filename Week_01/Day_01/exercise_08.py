# NÍVEL DIFÍCIL 🔴
# EXERCÍCIO 8: Sistema de Controle de Estoque
# Contexto: Empresas precisam gerenciar produtos.
# Tarefa: Crie um sistema com:

# Lista de produtos (cada produto é uma lista: [nome, quantidade, preço])
# Menu:

# Adicionar produto
# Listar produtos
# Buscar produto por nome
# Calcular valor total do estoque
# Sair



# Dicas:

# Use lista dentro de lista
# Para buscar, use for e if com in ou ==
# Valor total = soma de (quantidade * preço) de cada produto
# Use try/except para evitar erros de digitação





produtos = []

while True:
    print('\n1 - Adicionar Produto')
    print('2 - Listar')
    print('3 - Buscar Produto')
    print('4 - Valor total do estoque')
    print('5 - Sair')
    
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        try:
            nome_produto = input('Digite o nome do produto: ')
            quantidade_produto = int(input('Digite a quantidade do produto em estoque: '))
            valor_produto = float(input('Digite o preço do produto: '))
            produto = [nome_produto, quantidade_produto, valor_produto]
            produtos.append(produto)

        except ValueError:
            print('Somente números!')
    elif opcao == '2':
        if len(produtos) == 0:
            print('Nenhum produto cadastrado.')
        else:
            print('\nLista de produtos:')
            for produto in produtos:
                print(f'Nome: {produto[0]}')
                print(f'Quantidade: {produto[1]}')
                print(f'Preço: R${produto[2]:.2f}')
                print('-' * 20)
    elif opcao == '3':
        nome_busca = input('Digite o nome do produto para buscar: ')

        encontrado = False

        for produto in produtos:
            if produto[0].lower() == nome_busca.lower():
                print('Produto encontrado!')
                print(f'Nome: {produto[0]}')
                print(f'Quantidade: {produto[1]}')
                print(f'Preço: R${produto[2]:.2f}')
                encontrado = True

        if not encontrado:
            print('Produto não encontrado. ')

    elif opcao == '4':
        if len(produtos) == 0:
            print('Nenhum produto cadastrado.')
        else:
            total = 0
            for produto in produtos:
                total += produto[1] * produto[2]

            print(f'O valor total do estoque: R${total:.2f}')

    elif opcao == '5':
        print('Saindo do programa...')
        break

    else:
        print('Nenhuma das opções está correta!')
 