"""
TaskTracker - Aplicacao CLI de gerenciamento de tarefas.

Bootcamp II - Fase 2 (Entrega Intermediaria)
Autor: Joao Pedro Vieira de Oliveira

Implementa o algoritmo planejado na Fase 1:
menu continuo, cadastro de tarefas com validacao de dados
e listagem dos registros armazenados em memoria.
"""

# Prioridades aceitas pelo sistema. A chave e a versao normalizada
# (minuscula e sem acento) e o valor e o rotulo exibido ao usuario.
PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "media": "Média",
    "média": "Média",
    "baixa": "Baixa",
}

STATUS_INICIAL = "Pendente"


def exibir_menu():
    """Imprime o menu principal da aplicacao."""
    print("\n" + "=" * 40)
    print("        TASKTRACKER - MENU PRINCIPAL")
    print("=" * 40)
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicacao")
    print("=" * 40)


def ler_titulo():
    """
    Le o titulo da tarefa.

    Regra de negocio: campo obrigatorio. Entradas vazias ou compostas
    apenas por espacos em branco sao rejeitadas e o prompt se repete.
    """
    while True:
        titulo = input("Titulo da tarefa: ").strip()
        if titulo:
            return titulo
        print("[ERRO] O titulo e obrigatorio e nao pode ficar em branco.")


def ler_prioridade():
    """
    Le a prioridade da tarefa.

    Regra de negocio: validacao estrita. Aceita exclusivamente
    Alta, Media (ou Média) e Baixa, ignorando maiusculas/minusculas.
    """
    while True:
        entrada = input("Prioridade (Alta / Media / Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("[ERRO] Prioridade invalida. Use apenas: Alta, Media ou Baixa.")


def cadastrar_tarefa(tarefas):
    """Coleta os dados, aplica as validacoes e adiciona a tarefa a lista."""
    print("\n--- CADASTRO DE NOVA TAREFA ---")

    titulo = ler_titulo()
    descricao = input("Descricao: ").strip()
    prioridade = ler_prioridade()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": STATUS_INICIAL,
    }

    tarefas.append(tarefa)
    print(f"\n[OK] Tarefa '{titulo}' cadastrada com status '{STATUS_INICIAL}'.")


def visualizar_tarefas(tarefas):
    """Exibe todas as tarefas cadastradas ou avisa que a lista esta vazia."""
    print("\n--- TAREFAS CADASTRADAS ---")

    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa #{indice}")
        print(f"  Titulo......: {tarefa['titulo']}")
        print(f"  Descricao...: {tarefa['descricao'] or '(sem descricao)'}")
        print(f"  Prioridade..: {tarefa['prioridade']}")
        print(f"  Data limite.: {tarefa['data_limite'] or '(nao informada)'}")
        print(f"  Status......: {tarefa['status']}")

    print(f"\nTotal de tarefas: {len(tarefas)}")


def main():
    """Loop principal da aplicacao."""
    tarefas = []

    print("Bem-vindo(a) ao TaskTracker!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Ate logo!")
            break
        else:
            print("\n[ERRO] Opcao invalida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
