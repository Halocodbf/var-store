import datetime

class OperacoesVenda:
    def __init__(self, estoque):
        self.estoque = estoque
        self.vendas_realizadas = []

    def registrar_venda(self):
        print("\n=== REGISTRO DE VENDA ===")
        codigo = input("Digite o código do produto: ")

        produto = self.estoque.buscar_produto(codigo)
        if not produto:
            print("Produto não encontrado.")
            return

        print(f"Produto: {produto.nome_produto} | Estoque atual: {produto.quantidade}")


        try:
            quantidade = int(input("Digite a quantidade vendida: "))
            if quantidade <= 0:
                print("Quantidade inválida.")
                return
        except ValueError:
            print("Digite um número válido para quantidade.")
            return

        # Verifica e atualiza o estoque automaticamente
        if produto.quantidade < quantidade:
            print(" Quantidade insuficiente em estoque.")
            return

        produto.quantidade -= quantidade
        valor_total = produto.preco.preco_final * quantidade

        # Salva a venda
        venda = {
            "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "produto": produto.nome_produto,
            "codigo": produto.codigo,
            "quantidade": quantidade,
            "preco_unitario": produto.preco.preco_final,
            "valor_total": valor_total
        }
        self.vendas_realizadas.append(venda)

        # Gera recibo automaticamente
        self.gerar_recibo(venda)
        print(" Venda registrada e recibo emitido com sucesso.")

    def gerar_recibo(self, venda):
        print("\n=== RECIBO DE VENDA ===")
        print(f"Data: {venda['data']}")
        print(f"Produto: {venda['produto']} (Cód: {venda['codigo']})")
        print(f"Quantidade vendida: {venda['quantidade']}")
        print(f"Preço unitário: R${venda['preco_unitario']:,.2f}")
        print(f"Valor total: R${venda['valor_total']:,.2f}")
        print("========================\n")

    def listar_vendas(self):
        if not self.vendas_realizadas:
            print("Nenhuma venda registrada.")
            return

        print("\n=== HISTÓRICO DE VENDAS ===")
        for v in self.vendas_realizadas:
            print(f"[{v['data']}] {v['produto']} - {v['quantidade']} un. | Total: R${v['valor_total']:,.2f}")

