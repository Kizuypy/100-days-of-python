# 📌 Day 06 - Exercícios de Python (Comprehensions Avançados)

## Resumo do dia

Hoje pratiquei **dict comprehension, set comprehension e isinstance()** — ferramentas mais avançadas para transformar e validar dados de forma compacta e eficiente.

---

## Exercícios Realizados

| Nº | Exercício | Contexto | Nível | Conceitos Praticados |
|----|-----------|----------|-------|---------------------|
| 1 | Dictionary Comprehension Básico | Criação de dicionários | Fácil 💚 | Dict comprehension, zip(), transformações |
| 2 | Set Comprehension e Duplicatas | Análise de texto | Médio 🧡 | Set comprehension, len(), split() |
| 3 | Verificador de Tipos | Separação de dados | Médio 🧡 | isinstance(), múltiplas verificações |
| 4 | Inverter Dicionário | Transformação de dados | Médio 🧡 | Dict comprehension, inversão chave-valor |
| 5 | Filtrar Alunos Aprovados | Filtragem de dados | Médio 🧡 | Dict comprehension com condição |

---

## Detalhes dos Exercícios

### 💚 Exercício 1: Dictionary Comprehension Básico
Criar dicionários usando comprehension em diferentes cenários.
- **Aprendizado principal:** Sintaxe `{chave: valor for item in lista}`
- **Casos praticados:** quadrados, zip de listas, filtros, transformações

### 🧡 Exercício 2: Set Comprehension
Extrair tamanhos únicos de palavras usando set comprehension.
- **Input:** frase longa
- **Output:** conjunto com tamanhos únicos
- **Aprendizado:** Sets removem duplicatas automaticamente

### 🧡 Exercício 3: Verificador de Tipos
Separar lista mista por tipos usando isinstance().
- **Input:** `[10, 3.14, "python", True, [1,2], ...]`
- **Output:** dicionário separando por tipo
- **Aprendizado:** Ordem importa! Bool antes de int

### 🧡 Exercício 4: Inverter Dicionário
Trocar chaves por valores usando dict comprehension.
- **Input:** `{"arroz": 20.50, "feijão": 8.90, ...}`
- **Output:** `{20.5: "arroz", 8.9: "feijão", ...}`
- **Aprendizado:** `.items()` retorna pares (chave, valor)

### 🧡 Exercício 5: Filtrar Alunos
Criar novo dicionário apenas com aprovados (nota >= 7).
- **Input:** dicionário aluno → nota
- **Output:** apenas aprovados
- **Aprendizado:** Dict comprehension com `if`

---

## Conteúdo estudado (curso)

Assisti às aulas sobre:
- List comprehension com mais de um `for`
- Mais detalhes sobre list comprehension
- Dictionary Comprehension e Set Comprehension
- isinstance() - para saber se objeto é de determinado tipo
- Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
- dir, hasattr e getattr em Python
- Mais detalhes sobre Iterables e Iterators (Iteráveis e Iteradores)

---

## Notas do dia

📖 [Ver notas detalhadas](NOTES.md)

---

## Progresso Geral

✅ Day 01 concluído  
✅ Day 02 concluído  
✅ Day 03 concluído  
✅ Day 04 concluído  
✅ Day 05 concluído  
✅ Day 06 concluído  
⬜ Day 07  

**Week 01 quase completa!** 🎉

---

💡 **Próximo passo:** Projeto prático no fim de semana aplicando tudo da semana!