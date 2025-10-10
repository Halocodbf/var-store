import datetime

class Venda:
    def __init__(self):
        self.data_hora = datetime.datetime.now()
        self.produtos_vendidos = []
        self.valor_total = 0.0

    def adicionar_produto(self, produto, quantidade):
        preco_venda = produto.preco.preco_final
        self.produtos_vendidos.append({
            "codigo": produto.codigo.codigo,
            "nome": produto.nome.nome_produto,
            "quantidade": quantidade,
            "preco_unitario": preco_venda,
            "subtotal": preco_venda * quantidade
        })
        self.valor_total += preco_venda * quantidade

    def __str__(self):
        detalhes_produtos = "\n".join(
            f"    - Cód: {p['codigo']}, Produto: {p['nome']}, Qtd: {p['quantidade']}, "
            f"Preço Unit.: R${p['preco_unitario']:,.2f}, Subtotal: R${p['subtotal']:,.2f}"
            for p in self.produtos_vendidos
        )
        return (f"Venda realizada em: {self.data_hora.strftime('%d/%m/%Y %H:%M:%S')}\n"
                f"  Valor Total: R${self.valor_total:,.2f}\n"
                f"  Itens:\n{detalhes_produtos}")


class RegistroVendas:
    def __init__(self):
        self.historico_vendas = []

    def registrar_venda(self, venda):
        self.historico_vendas.append(venda)
        print("\nVenda registrada com sucesso!")

    def gerar_relatorio(self):
        print("\n=== Relatório de Vendas ===")
        if not self.historico_vendas:
            print("Nenhuma venda registrada.")
            return

        for venda in self.historico_vendas:
            print(venda)
            print("-" * 30)


class Estoque:
    def __init__(self):
        self.produtos = {}

    def cadastrar_produto(self, produto):
        if produto.codigo.codigo in self.produtos:
            print("Produto com este código já existe.")
        else:
            self.produtos[produto.codigo.codigo] = produto
            print("Produto cadastrado com sucesso!")

    def adicionar_estoque(self, codigo, quantidade):
        if codigo in self.produtos:
            self.produtos[codigo].quantidade.quantidade += quantidade
            print("Estoque atualizado.")
        else:
            print("Produto não encontrado.")

    def remover_estoque(self, codigo, quantidade):
        if codigo in self.produtos:
            if self.produtos[codigo].quantidade.quantidade >= quantidade:
                self.produtos[codigo].quantidade.quantidade -= quantidade
                return True
            else:
                print("Quantidade insuficiente em estoque.")
                return False
        else:
            print("Produto não encontrado.")
            return False

    def ajustar_estoque(self, codigo, nova_quantidade):
        if codigo in self.produtos:
            self.produtos[codigo].quantidade.quantidade = nova_quantidade
            print("Estoque ajustado.")
        else:
            print("Produto não encontrado.")

    def listar_produtos(self):
        print("\n=== Produtos em Estoque ===")
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        for produto in self.produtos.values():
            print(produto)
            if produto.quantidade.quantidade < 5:
                print("Estoque baixo!")

    def buscar_produto(self, codigo):
        return self.produtos.get(codigo, None)

    def realizar_venda(self, registro_vendas):
        nova_venda = Venda()
        while True:
            codigo = input("Digite o código do produto (ou 'fim' para finalizar a venda): ")
            if codigo.lower() == 'fim':
                break
            
            produto = self.buscar_produto(codigo)
            if not produto:
                print("Produto não encontrado.")
                continue

            try:
                quantidade = int(input(f"Digite a quantidade para o produto '{produto.nome.nome_produto}': "))
                if quantidade <= 0:
                    print("A quantidade deve ser positiva.")
                    continue
            except ValueError:
                print("Quantidade inválida.")
                continue
            
            if produto.quantidade.quantidade >= quantidade:
                nova_venda.adicionar_produto(produto, quantidade)
                print(f"-> Produto '{produto.nome.nome_produto}' adicionado à venda.")
            else:
                print(f"Estoque insuficiente para '{produto.nome.nome_produto}'. "
                      f"Disponível: {produto.quantidade.quantidade}")

        if not nova_venda.produtos_vendidos:
            print("Venda cancelada pois nenhum produto foi adicionado.")
            return

        for item in nova_venda.produtos_vendidos:
            self.remover_estoque(item['codigo'], item['quantidade'])
        
        registro_vendas.registrar_venda(nova_venda)