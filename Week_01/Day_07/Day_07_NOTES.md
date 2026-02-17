# 📝 Notas - Day 07

## Como foi o dia

Foi muito bom e desafiador. Generators e tratamento de exceções são conceitos bem diferentes do que vinha fazendo até agora.

É muito importante entender sobre erros e como tratá-los. Até hoje eu meio que ignorava essa parte, mas percebi que em aplicações reais, saber lidar com erros é essencial. Não dá pra simplesmente deixar o programa quebrar quando algo dá errado.

Generators foram estranhos no começo — a ideia de `yield` ao invés de `return` é diferente. Mas quando entendi que é sobre economizar memória e gerar valores sob demanda, fez sentido.

---

## O que realmente aprendi hoje

**Generators (Geradores):**
- Funções que usam `yield` ao invés de `return`
- Geram valores sob demanda (um de cada vez)
- Economizam MUITA memória (não carregam tudo de uma vez)
- Úteis para sequências grandes ou infinitas
- Usa-se `next()` ou `for` loop para consumir valores
- Sintaxe: `def funcao(): yield valor`

**Generator Expressions:**
- Similar a list comprehension mas com `()`: `(x for x in range(10))`
- Mais eficiente em memória que listas

**Try/Except (Tratamento de Exceções):**
- `try:` → código que pode dar erro
- `except TipoDeErro:` → o que fazer quando der erro específico
- `except:` → pega qualquer erro (não recomendado)
- `finally:` → sempre executa, mesmo com erro
- `else:` → executa só se NÃO der erro

**Exceções Comuns:**
- `ZeroDivisionError` → divisão por zero
- `IndexError` → índice fora do range da lista
- `TypeError` → tipo errado (ex: somar string com int)
- `FileNotFoundError` → arquivo não existe
- `ValueError` → valor inválido (ex: int("abc"))

**Boas Práticas:**
- Sempre tratar erros específicos (não usar `except:` genérico)
- Usar `finally` para fechar arquivos/conexões
- Não silenciar erros — avisar o usuário
- Generator é melhor que lista quando dados são grandes

---

## Exercícios praticados

* **Total:** 5 exercícios
* **Níveis:** Fácil 💚 (2), Médio 🧡 (2), Difícil ❤️ (1)
* **Foco:** generators, yield, try/except, tratamento de erros

---

## O que ainda preciso melhorar

- Entender melhor quando usar generator vs lista normal
- Praticar mais tratamento de múltiplas exceções
- Aprender sobre criar minhas próprias exceções (raise)
- Ver generators mais complexos (com send, throw, close)

---

## Reflexão final

Hoje foi cansativo mas produtivo. Generators e exceções são ferramentas que todo programador precisa dominar. Não adianta saber fazer o código funcionar se ele quebra na primeira coisa inesperada.

**Week 01 COMPLETA!** 🎉 7 dias seguidos de estudo e prática. Agora vem o projeto do fim de semana pra consolidar tudo!

---

💡 **Conquista desbloqueada:** Week 01 finalizada! Próximo passo: projeto prático!