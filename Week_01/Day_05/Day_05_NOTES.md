# 📝 Notas - Day 05

## Como foi o dia

Hoje foi tranquilo. Diferente dos dias anteriores com dicionários e funções que me confundiram bastante, lambda e list comprehension foram mais suaves de entender.

Não sei se é porque já estou me acostumando com a sintaxe do Python ou se esses conceitos realmente são mais intuitivos, mas consegui fazer os exercícios sem tanto travamento. Foi bom ter um dia assim depois de dias mais pesados.

---

## O que realmente aprendi hoje

**Sobre Lambda (funções anônimas):**
- Lambda é uma função de uma linha só: `lambda x: x * 2`
- Equivale a criar uma função def mas de forma compacta
- Útil para operações simples e rápidas
- Sintaxe: `lambda parametros: expressão`

**Sobre Map:**
- `map()` aplica uma função em todos os itens de uma lista
- Retorna um objeto map (precisa converter pra lista com `list()`)
- Uso: `list(map(funcao, lista))`
- Substitui loops `for` em muitos casos

**Sobre Filter:**
- `filter()` filtra itens baseado em uma condição (True/False)
- Também retorna um objeto que precisa ser convertido pra lista
- Uso: `list(filter(funcao_condicao, lista))`
- A função deve retornar True ou False

**Sobre List Comprehension:**
- Forma compacta de criar listas: `[expressão for item in lista]`
- Pode ter condição: `[expressão for item in lista if condicao]`
- Substitui `map()` e `filter()` de forma mais legível
- Exemplo: `[x**2 for x in range(10) if x % 2 != 0]`

**Truques que aprendi:**
- `math.ceil()` arredonda pra cima
- `len()` funciona em strings pra contar letras
- Lambda pode ser atribuída a variável: `dobrar = lambda x: x * 2`
- List comprehension é geralmente mais "pythônico" que map/filter

---

## Exercícios praticados

* **Total:** 5 exercícios
* **Níveis:** Fácil 💚 (2), Médio 🧡 (3)
* **Foco:** lambda, map, filter, list comprehension

---

## O que ainda preciso melhorar

- Decidir quando usar lambda vs função normal
- Entender melhor quando list comprehension é melhor que map/filter
- Praticar list comprehension com estruturas mais complexas
- Ver dict comprehension e set comprehension também

---

## Reflexão final

Dia tranquilo, exercícios fluíram bem. Lambda e list comprehension parecem ferramentas poderosas que vão simplificar muito meu código. Gostei de ver que nem todo dia precisa ser uma batalha — às vezes as coisas simplesmente funcionam. 

Vamos pro próximo! 💪

---

💡 **Lembrete:** Mantendo o ritmo de 5 exercícios por dia. Consistência é a chave!