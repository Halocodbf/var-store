import datetime

historico = []

def registrar_movimento(nome, quantidade, tipo):
    """Registra um movimento no histórico."""
    data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    historico.append({
        "data": data,
        "produto": nome,
        "quantidade": quantidade,
        "tipo": tipo
    })

def relatorio_estoque(estoque):
    """Exibe o relatório atual do estoque."""
    print("\n=== RELATÓRIO DE ESTOQUE ===")
    if not estoque.produtos:
        print("Nenhum produto no estoque.")
    else:
        for produto, obj in estoque.produtos.items():
            print(f"{obj.nome_produto}: {obj.quantidade} unidade(s)")

def historico_movimentos():
    """Exibe o histórico de todas as movimentações."""
    print("\n=== HISTÓRICO DE MOVIMENTOS ===")
    if not historico:
        print("Nenhum movimento registrado.")
    else:
        for mov in historico:
            print(f"[{mov['data']}] {mov['tipo']} - {mov['produto']} ({mov['quantidade']} un)")
