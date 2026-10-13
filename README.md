# TaskTracker

Aplicação de linha de comando (CLI) para cadastro e acompanhamento de tarefas, desenvolvida como entrega da **Fase 2 (Etapa Intermediária)** do Bootcamp II — Engenharia de Software, Versionamento Profissional de Código e Desenvolvimento de Sistemas.

O projeto traduz para código Python o planejamento lógico e a arquitetura de dados definidos na Fase 1.

---

## Descrição funcional

O TaskTracker roda inteiramente no terminal e apresenta um menu contínuo com três opções:

| Opção | Ação |
|-------|------|
| 1 | Cadastrar nova tarefa |
| 2 | Visualizar tarefas cadastradas |
| 3 | Sair da aplicação |

Cada tarefa é armazenada em memória como um dicionário com os seguintes campos:

| Campo | Tipo | Regra |
|-------|------|-------|
| Título | String | **Obrigatório.** Entradas vazias ou compostas apenas por espaços são rejeitadas e o prompt se repete até receber um título válido. |
| Descrição | String | Detalhamento livre da tarefa. |
| Prioridade | String | **Validação estrita.** Aceita apenas `Alta`, `Media` (ou `Média`) e `Baixa`. Qualquer outra entrada gera mensagem de erro e repete o prompt. |
| Data limite | String | Data planejada para conclusão (formato `DD/MM/AAAA`). |
| Status | String | Definido automaticamente como `Pendente` no momento do cadastro. |

Na listagem, se nenhuma tarefa tiver sido cadastrada, o programa informa que não existem registros no momento. Caso contrário, percorre a lista e exibe todas as propriedades de cada tarefa de forma organizada.

---

## Tecnologias utilizadas

- **Python 3** — linguagem da aplicação (biblioteca padrão apenas, sem dependências externas)
- **Git** — versionamento local
- **GitHub** — repositório remoto e rastreabilidade do histórico de commits

---

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md                    # Documentação principal da aplicação e instruções de uso
├── .gitignore                   # Regras para ignorar arquivos temporários do Python e ambiente virtual
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico e arquitetural entregue na Fase 1
└── src/
    └── main.py                  # Código-fonte principal da aplicação TaskTracker
```

---

## Instalação

Pré-requisito: **Python 3.8 ou superior** instalado na máquina.

```bash
# 1. Clonar o repositório
git clone https://github.com/jpvoliveir/tasktracker-projeto.git

# 2. Entrar na pasta do projeto
cd tasktracker-projeto
```

Não há dependências externas a instalar — a aplicação usa apenas a biblioteca padrão do Python.

---

## Execução

A partir da raiz do projeto:

```bash
python src/main.py
```

Em sistemas onde o comando `python` aponta para o Python 2, use:

```bash
python3 src/main.py
```

---

## Exemplo de uso

```
========================================
        TASKTRACKER - MENU PRINCIPAL
========================================
1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicacao
========================================
Escolha uma opcao: 1

--- CADASTRO DE NOVA TAREFA ---
Titulo da tarefa:
[ERRO] O titulo e obrigatorio e nao pode ficar em branco.
Titulo da tarefa: Estudar Docker
Descricao: Preparar o ambiente para a Fase 3 do Bootcamp
Prioridade (Alta / Media / Baixa): urgente
[ERRO] Prioridade invalida. Use apenas: Alta, Media ou Baixa.
Prioridade (Alta / Media / Baixa): alta
Data limite (DD/MM/AAAA): 30/11/2026

[OK] Tarefa 'Estudar Docker' cadastrada com status 'Pendente'.
```

---

## Próximos passos (Fase 3)

- Empacotamento da aplicação
- Containerização com Docker
- Testes automatizados e deploy

---

## Autor

**João Pedro Vieira de Oliveira**
Bootcamp II — Fase 2 (Entrega Intermediária)
