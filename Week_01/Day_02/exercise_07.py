# NÍVEL DIFÍCIL 🔴
# EXERCÍCIO 7: Sistema de Validação de CPF com Histórico
# Contexto: Muitas empresas precisam validar CPF de clientes/funcionários.
# Tarefa: Crie um programa com menu:

# 1. Validar CPF:
#    - Peça o CPF (apenas números, deve ter 11 dígitos)
#    - Calcule os 2 dígitos verificadores (igual ao nível fácil)
#    - Diga se é válido ou inválido
#    - Se válido, pergunte o nome da pessoa e armazene: [nome, cpf]

# 2. Listar CPFs validados:
#    - Mostre todos os CPFs válidos salvos
#    - Formato: "João Silva - 123.456.789-10"
#    - Formate o CPF com pontos e hífen para exibir

# 3. Sair

# DICA DE FORMATAÇÃO:
# cpf = "12345678910"
# cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
# Resultado: "123.456.789-10"







cpfs_validados = []

while True:
    print("\n=== Menu ===")
    print("1 - Validar CPF")
    print("2 - Listar CPFs validados")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ").strip()


    if opcao == "1":
        cpf = input("Digite o CPF (apenas números): ").strip()

        if not cpf.isdigit() or len(cpf) != 11:
            print("CPF inválido! deve conter exatamente 11 números")
            continue

        if cpf == cpf[0] * 11:
            print("CPF INVÁLIDO")
            continue
        
        soma = 0
        peso = 10

        for numero in cpf[:9]:
            soma += int(numero) * peso
            peso -= 1

        resto =  (soma * 10) % 11
        primeiro_digito = 0 if resto > 9 else resto

        soma = 0
        peso = 11

        for numero in cpf[:10]:
            soma += int(numero) * peso
            peso -= 1

        resto = (soma * 10) % 11
        segundo_digito = 0 if resto > 9 else resto


        if cpf[-2:] == f"{primeiro_digito}{segundo_digito}":
            print('CPF válido!')

            nome = input("Digite o nome da pessoa: ").strip()

            cpfs_validados.append([nome, cpf])


        else:
            print("CPF INVÁLIDO!")
    elif opcao == "2":
        if not cpfs_validados:
            print("Nenhum CPF validado ainda.")
        else:
            print("\n==== CPFs VALIDADOS ====")
            for pessoa in cpfs_validados:
                nome = pessoa[0]
                cpf = pessoa[1]

                cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
                print(f"{nome} - {cpf_formatado}")
    elif opcao == "3":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida! Digite 1, 2 ou 3")