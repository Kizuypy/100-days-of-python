# 🧡 MÉDIO 1: Inversor de Dicionário
# Contexto: Às vezes precisamos trocar chaves por valores em dicionários.
# Tarefa: Crie uma função inverter_dicionario(dic) que:

# Receba um dicionário onde valores são únicos
# Retorne um novo dicionário onde chaves viram valores e valores viram chaves


def inverter_dicionario(dic):
    novo = {}
    for chave, valor in dic.items():
        novo[valor] = chave
    return novo

d = {"a": 1, "b": 2, "c": 3}
print(inverter_dicionario(d))

