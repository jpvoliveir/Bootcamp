# TaskTracker

Aplicação de linha de comando (CLI) para cadastro e acompanhamento de tarefas, desenvolvida ao longo do Bootcamp II — Engenharia de Software, Versionamento Profissional de Código e Desenvolvimento de Sistemas.

O projeto evoluiu em três fases: o planejamento lógico (Fase 1), a implementação em Python com versionamento (Fase 2) e a containerização com Docker (Fase 3).

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

- **Python 3.11** — linguagem da aplicação (biblioteca padrão apenas, sem dependências externas)
- **Docker** — empacotamento da aplicação em imagem autossuficiente
- **Docker Compose** — orquestração da execução interativa da CLI
- **Git / GitHub** — versionamento e rastreabilidade do histórico de commits

---

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md                    # Documentação da aplicação e guia de execução
├── .gitignore                   # Regras para arquivos temporários do Python e ambiente virtual
├── Dockerfile                   # Receita de construção da imagem da aplicação
├── docker-compose.yml           # Orquestração da execução interativa do container
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico e arquitetural (Fase 1)
└── src/
    └── main.py                  # Código-fonte principal da aplicação TaskTracker
```

---

## Execução com Docker (recomendado)

Pré-requisito: **Docker** instalado e em execução.

```bash
git clone https://github.com/jpvoliveir/Bootcamp.git
cd Bootcamp
```

### 1. Construir a imagem

```bash
docker build -t tasktracker-app .
```

### 2. Rodar o container em modo isolado

```bash
docker run -it tasktracker-app
```

### 3. Rodar via orquestração (recomendado)

```bash
docker compose run --rm tasktracker-app
```

> **Por que as flags `-it`?**
> A aplicação é interativa e depende de `input()` para ler o que o usuário digita. Um container roda isolado por padrão, sem canal de entrada e sem terminal. A flag `-i` (`stdin_open`) mantém o canal de entrada aberto e a flag `-t` (`tty`) aloca um terminal virtual. Sem elas, o programa encerra imediatamente ao tentar ler a primeira entrada.
>
> No `docker-compose.yml` essas duas condições estão declaradas como `stdin_open: true` e `tty: true`, por isso o comando de orquestração já sobe o container pronto para interação.

---

## Execução local sem Docker

Pré-requisito: **Python 3.8 ou superior**.

```bash
python src/main.py
```

Em sistemas onde o comando `python` aponta para o Python 2, use `python3 src/main.py`.

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

## Observação sobre persistência

Os dados são mantidos apenas em memória durante a execução. Ao encerrar a aplicação — ou ao parar o container — as tarefas cadastradas são descartadas. A persistência em arquivo ou banco de dados está fora do escopo definido no planejamento da Fase 1.

---

## Autor

**João Pedro Vieira de Oliveira**
Bootcamp II — Ciência da Computação, CEUB
