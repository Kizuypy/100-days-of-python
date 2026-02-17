# 📌 Day 07 - Exercícios de Python (Generators e Exceções)

## Resumo do dia

Hoje pratiquei **generators com yield e tratamento de exceções** — conceitos fundamentais para escrever código eficiente e robusto que não quebra ao encontrar erros.

---

## Exercícios Realizados

| Nº | Exercício | Contexto | Nível | Conceitos Praticados |
|----|-----------|----------|-------|---------------------|
| 1 | Generator de Countdown | Sequências | Fácil 💚 | yield, while, generators básicos |
| 2 | Divisão Segura | Tratamento de erros | Fácil 💚 | try/except, ZeroDivisionError |
| 3 | Generator de Fibonacci | Sequências matemáticas | Médio 🧡 | yield, múltiplas variáveis, lógica |
| 4 | Acesso Seguro a Listas | Validação de dados | Médio 🧡 | Múltiplas exceções, IndexError, TypeError |
| 5 | Leitura de Arquivo por Linha | I/O eficiente | Difícil ❤️ | Generator, FileNotFoundError, finally |

---

## Detalhes dos Exercícios

### 💚 Exercício 1: Generator de Countdown
Criar generator que faz contagem regressiva.
- **Input:** número inicial
- **Output:** sequência de n até 0
- **Aprendizado:** Generators com `yield` são iteráveis

### 💚 Exercício 2: Divisão Segura
Função que divide números tratando divisão por zero.
- **Erro tratado:** `ZeroDivisionError`
- **Retorno:** resultado ou `None`
- **Aprendizado:** Try/except evita que programa quebre

### 🧡 Exercício 3: Generator de Fibonacci
Generator que gera sequência de Fibonacci até limite.
- **Input:** limite máximo
- **Output:** 0, 1, 1, 2, 3, 5, 8, 13...
- **Aprendizado:** Generators para sequências matemáticas

### 🧡 Exercício 4: Acesso Seguro a Listas
Função que acessa lista tratando múltiplos erros.
- **Erros tratados:** `IndexError`, `TypeError`
- **Aprendizado:** Múltiplos `except` para diferentes erros

### ❤️ Exercício 5: Leitura Eficiente de Arquivo
Generator que lê arquivo linha por linha sem carregar tudo na memória.
- **Erro tratado:** `FileNotFoundError`
- **Usa:** `finally` para garantir fechamento do arquivo
- **Aprendizado:** Generators economizam memória em arquivos grandes

---

## Conteúdo estudado (curso)

Assisti às aulas sobre:
- Generator expression, Iterables e Iterators em Python
- Introdução às Generator functions em Python
- yield from em generator functions
- (Parte 1) try e except para tratar exceções
- (Parte 2) try e except para tratar exceções
- try, except, else e finally + Built-in Exceptions
- raise - lançando exceções (erros)
- Módulos - import, from, as e *

---

## Notas do dia

📖 [Ver notas detalhadas](NOTES.md)

---

## 🎉 PROGRESSO GERAL - WEEK 01 COMPLETA!

✅ Day 01 - Cadastros e validações  
✅ Day 02 - Upgrades e refatoração  
✅ Day 03 - Funções  
✅ Day 04 - Dicionários e Sets  
✅ Day 05 - Lambda e List Comprehension  
✅ Day 06 - Dict/Set Comprehension  
✅ Day 07 - Generators e Exceções  

**🏆 WEEK 01 FINALIZADA!**

---

## 📊 Estatísticas da Semana

- **Total de exercícios:** 40 exercícios
- **Dias consecutivos:** 7 dias
- **Conceitos aprendidos:** 
  - Estruturas básicas (if, for, while)
  - Listas, dicionários, sets
  - Funções e lambda
  - Comprehensions
  - Generators
  - Tratamento de exceções

---

💡 **Próximo passo:** Projeto prático do fim de semana aplicando tudo da Week 01!