# NÍVEL FÁCIL 💚
# EXERCÍCIO 2: Validação de Login Simples
# Contexto: Sistemas corporativos precisam validar credenciais.
# Tarefa: Crie um programa que:

# Tenha um usuário e senha fixos no código (pode ser "admin" e "1234")
# Peça ao usuário para digitar usuário e senha
# Se estiver correto, mostre "Login realizado com sucesso!"
# Se errado, mostre "Usuário ou senha incorretos"

usuario_correto = 'admin'
senha_correta = '1234'


usuario = input('Digite o usuário para entrar: ')
senha = input('Digite a senha para poder entrar: ')


if usuario != usuario_correto or senha != senha_correta:
    print('Usuário ou senha incorretos')
else: 
    print('Login realizado com sucesso!')
