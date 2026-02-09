# NÍVEL DIFÍCIL 🔴
# EXERCÍCIO 8: Sistema de Controle de Estoque com Alertas
# Contexto: Empresas precisam gerenciar produtos e evitar falta de estoque.
# Tarefa: Crie um sistema com menu:

# 1. Adicionar produto:
#    - Nome (não pode ser vazio)
#    - Quantidade em estoque (deve ser >= 0)
#    - Preço unitário (deve ser > 0)
#    - Estoque mínimo (quantidade de alerta)
#    - Armazene: [nome, quantidade, preço, estoque_minimo]

# 2. Listar produtos:
#    - Mostre todos com: nome, quantidade, preço, valor total (qtd × preço)
#    - Se quantidade < estoque_minimo, mostre "⚠️ ESTOQUE BAIXO!"

# 3. Atualizar estoque:
#    - Busque produto por nome
#    - Pergunte: adicionar ou remover?
#    - Atualize a quantidade
#    - Não permita quantidade negativa

# 4. Relatório do estoque:
#    - Valor total de todos os produtos
#    - Produtos com estoque baixo (quantidade < estoque_minimo)

# 5. Sair





produtos = []

while True:
    print('\n Escolha uma das opções a baixo: ')

    opcao = input('1 - Adicionar Produto\n'
    '2 - Listar produtos\n'
    '3 - Atualizar Estoque\n'
    '4 - Relatório do estoque\n'
    '5 - Sair do programa ')

    if not opcao:
        print('Opção não pode estar vazia!')
        continue

    elif opcao == '1':
        while True:
            nome_produto = input('Digite o nome do produto: ').strip()
            if not nome_produto:
                print("O produto não pode estar vazio!")
            else:
                 break

        while True:
            try:
                quantidade_produto = int(input('Digite a quantidade em estoque do produto: '))
                if quantidade_produto <= 0:
                    print('Quantidade em estoque deve ser maior que Zero!')
                    continue
                break
            except ValueError:
                print('Digite um número válido!')
        while True:
            try:    
                preco_uni_produto = float(input("Digite o preço unitário do produto: "))
                if preco_uni_produto <= 0:
                    print('Preço unitário deve ser maior que zero! ')
                    continue
                break
            except ValueError:
                print('Digite um número válido!')    
        while True:
            try:
                estoque_min_produto = int(input("Digite o estoque mínimo do produto: "))
                if estoque_min_produto <= 0:
                    print('Estoque mínimo deve ser maior que zero!')
                    continue
                break
            except ValueError:
                    print('Digite um número válido!')
                
        produtos.append([nome_produto, quantidade_produto, preco_uni_produto, estoque_min_produto])
        print('Produtos:', produtos)

    elif opcao == '2':
        if len(produtos) == 0:
            print('Nenhum produto cadastrado!')
        else:
            valor_total = 0
            print("\n=== Produtos Cadastrados ===")
            for i, produto in enumerate(produtos,start=1):
                nome = produto[0]
                quantidade = produto[1]
                preco = produto[2]
                estoque_min_produto = produto[3]

                subtotal = preco * quantidade
                valor_total += subtotal

                if quantidade < estoque_min_produto:
                    mensagem = "⚠ Estoque Baixo!"
                else:
                    mensagem = ""
                
                print(f"{i}. Nome: {nome}")
                print(f"   Quantidade: {quantidade}")
                print(f"   Preço unitário: R$ {preco:.2f}")
                print(f"   Subtotal: R$ {subtotal:.2f}")
                if mensagem:
                    print(f'   {mensagem}')
                print("-" * 25)

            print(f"VALOR TOTAL EM ESTOQUE: R$ {valor_total:.2f}")  
    elif opcao == '3':
        if len(produtos) == 0:
            print("Nenhum produto cadastrado para atualizar!")
        else:
            nome_busca = input("Digite o nome do produto que deseja atualizar: ").strip()
            encontrado = False

            for produto in produtos:
                if produto[0].lower() == nome_busca.lower():  # busca ignorando maiúsculas/minúsculas
                    encontrado = True
                    print(f"Produto encontrado: {produto[0]} - Quantidade atual: {produto[1]}")
                    while True:
                        acao = input("Deseja adicionar ou remover estoque? (a/r): ").strip().lower()
                        if acao not in ['a', 'r']:
                            print("Digite 'a' para adicionar ou 'r' para remover!")
                            continue
                        break

                    while True:
                        try:
                            quantidade_atualizar = int(input("Digite a quantidade: "))
                            if acao == 'r' and quantidade_atualizar > produto[1]:
                                print("Não é possível remover mais do que existe no estoque!")
                                continue
                            if quantidade_atualizar < 0:
                                print("Quantidade não pode ser negativa!")
                                continue
                            break
                        except ValueError:
                            print("Digite um número válido!")

                    if acao == 'a':
                        produto[1] += quantidade_atualizar
                    else:
                        produto[1] -= quantidade_atualizar

                    print(f"Estoque atualizado! Nova quantidade: {produto[1]}")
                    break

            if not encontrado:
                print("Produto não encontrado!")

    elif opcao == '4':
        if len(produtos) == 0:
            print("Nenhum produto cadastrado!")
        else:
            valor_total_estoque = 0
            print("\n=== RELATÓRIO DO ESTOQUE ===")
            for i, produto in enumerate(produtos, start=1):
                nome = produto[0]
                quantidade = produto[1]
                preco = produto[2]
                estoque_min_produto = produto[3]

                subtotal = preco * quantidade
                valor_total_estoque += subtotal

                alerta = "⚠ Estoque Baixo!" if quantidade < estoque_min_produto else ""

                print(f"{i}. Nome: {nome}")
                print(f"   Quantidade: {quantidade}")
                print(f"   Preço unitário: R$ {preco:.2f}")
                print(f"   Valor total: R$ {subtotal:.2f}")
                if alerta:
                    print(f"   {alerta}")
                print("-" * 25)

            print(f"VALOR TOTAL DE TODOS OS PRODUTOS: R$ {valor_total_estoque:.2f}")

    elif opcao == '5':
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida! Digite um número de 1 a 5.")

                

