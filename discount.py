class Preco:
    def __init__(self, preco):
        self.preco_original = preco
        self.desconto_percentual = 0

    @property
    def preco_final(self):
        if self.desconto_percentual > 0:
            return self.preco_original * (1 - self.desconto_percentual / 100)
        return self.preco_original

    def aplicar_desconto(self, percentual):
        if 0 <= percentual <= 100:
            self.desconto_percentual = percentual
            print(f"Desconto de {percentual}% aplicado.")
        else:
            print("Percentual de desconto inválido. Deve ser entre 0 e 100.")

    def menu_info(self):
        if self.desconto_percentual > 0:
            return (f"Preço Original: R${self.preco_original:,.2f} | "
                    f"Desconto: {self.desconto_percentual}% | "
                    f"Preço Final: R${self.preco_final:,.2f}")
        return f"Preço: R${self.preco_final:,.2f}"


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

    def aplicar_desconto_produto(self, codigo, percentual):
        produto = self.buscar_produto(codigo)
        if produto:
            produto.preco.aplicar_desconto(percentual)
        else:
            print("Produto não encontrado.")


def aplicar_desconto_interativo(estoque):
    codigo = input("Digite o código do produto para aplicar o desconto: ")
    try:
        percentual = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))
        estoque.aplicar_desconto_produto(codigo, percentual)
    except ValueError:
        print("Valor inválido. O percentual de desconto deve ser um número.")