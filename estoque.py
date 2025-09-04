from Categoria import Quantidade_em_Estoque

class Estoque:
    def _init_(self):
        self.produtos = {}

    def cadastrar_produto(self, produto):
        if produto.codigo in self.produtos:
            print("Produto com este código já existe.")
        else:
            self.produtos[produto.codigo] = produto
            print("Produto cadastrado com sucesso!")

    def adicionar_estoque(self, codigo, quantidade):
        if codigo in self.produtos:
            self.produtos[codigo].quantidade += quantidade
            print("Estoque atualizado.")
        else:
            print("Produto não encontrado.")

    def remover_estoque(self, codigo, quantidade):
        if codigo in self.produtos:
            if self.produtos[codigo].quantidade >= quantidade:
                self.produtos[codigo].quantidade -= quantidade
                print("Quantidade removida do estoque.")
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Produto não encontrado.")

    def ajustar_estoque(self, codigo, nova_quantidade):
        if codigo in self.produtos:
            self.produtos[codigo].quantidade = nova_quantidade
            print("Estoque ajustado.")
        else:
            print("Produto não encontrado.")

    def listar_produtos(self):
        for produto in self.produtos.values():
            print(produto)
            if produto.quantidade < 5:
                print("⚠️  Estoque baixo!")

    def buscar_produto(self, codigo):
        return self.produtos.get(codigo, None)