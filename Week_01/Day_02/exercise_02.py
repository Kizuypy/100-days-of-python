# NÍVEL MÉDIO 🟡
# EXERCÍCIO 2: Sistema de Login com Tentativas
# Contexto: Sistemas corporativos precisam validar credenciais com segurança.
# Tarefa: Crie um programa que:

# 1. Tenha uma lista de usuários válidos cadastrados:
#    Exemplo: [["admin", "1234"], ["gerente", "5678"], ["operador", "abcd"]]

# 2. Peça ao usuário para digitar usuário e senha

# 3. Validações:
#    - Usuário não pode ser vazio
#    - Senha não pode ser vazia
#    - Se algum estiver vazio, peça novamente

# 4. Sistema de tentativas:
#    - O usuário tem no máximo 3 tentativas para acertar
#    - A cada erro, mostre: "Usuário ou senha incorretos. Tentativa X de 3"
#    - Se acertar, mostre: "Login realizado com sucesso! Bem-vindo, [USUÁRIO]"
#    - Se errar 3 vezes, mostre: "Acesso bloqueado! Muitas tentativas incorretas."

# 5. Após login bem-sucedido ou bloqueio, pergunte:
#    "Deseja tentar novamente? (s/n)"
#    - Se sim, reinicia o processo (3 tentativas novas)
#    - Se não, encerra o programa

# 6. EXTRA (opcional):
#    - Mostre quantas tentativas restam
#    - Não diferencie maiúsculas/minúsculas no usuário (admin = Admin = ADMIN)

usuarios_validos = [
    ["admin", "1234"],
    ["gerente", "5678"],
    ["operador", "abcd"]
]

while True:  

    tentativas = 1
    login_sucesso = False

    while tentativas <= 3:
        print(f'\nTentativa {tentativas} de 3')

        login_usuario = input('Digite o usuário: ').strip()
        login_senha = input('Digite a senha: ').strip()

        if not login_usuario or not login_senha:
            print('Usuário ou senha não podem estar vazios!')
            continue

        if [login_usuario, login_senha] in usuarios_validos:
            print(f'Login realizado com sucesso! Bem-vindo, {login_usuario.title()}')
            login_sucesso = True
            break
        else:
            print('Usuário ou senha incorretos!')
            tentativas += 1

    if not login_sucesso:
        print('\n❌ Conta bloqueada após 3 tentativas!')


    resposta = input('\nDeseja tentar novamente? (s/n): ').strip().lower()

    if resposta != 's':
        print('Encerrando sistema...')
        break


        


