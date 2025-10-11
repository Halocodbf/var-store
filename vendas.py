# Lista para armazenar as vendas realizadas
vendas = []

def registrar_venda(estoque):
    """
    Registra uma venda de produto, atualiza o estoque e armazena as informações da venda.
    """
    try:
        codigo = input("Digite o código do produto a vender: ")

        produto = estoque.buscar_produto(codigo)
        if not produto:
            print("Produto não encontrado.")
            return

        print(f"Produto encontrado: {produto.nome.nome_produto} | Estoque disponível: {produto.quantidade.quantidade}")

        quantidade_vendida = int(input("Digite a quantidade vendida: "))

        if quantidade_vendida <= 0:
            print("Quantidade inválida. Deve ser maior que zero.")
            return

        if quantidade_vendida > produto.quantidade.quantidade:
            print("Quantidade insuficiente em estoque.")
            return

        # Atualiza o estoque
        produto.quantidade.quantidade -= quantidade_vendida

        # Calcula o valor total da venda
        valor_total = quantidade_vendida * produto.preco.preco

        # Registra os dados da venda
        venda = {
            "produto": produto.nome.nome_produto,
            "codigo": produto.codigo.codigo,
            "quantidade_vendida": quantidade_vendida,
            "preco_unitario": produto.preco.preco,
            "valor_total": valor_total
        }
        vendas.append(venda)

        print(f"Venda registrada com sucesso. Valor total: R${valor_total:,.2f}")

    except ValueError:
        print("Erro: digite um número válido para a quantidade.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
