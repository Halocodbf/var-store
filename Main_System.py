# ==== Classe Produto (inalterada) ====
class Produto:
    def __init__(self, nome_produto, nome_marca, codigo, categoria, quantidade, preco, descricao, fornecedor):
        self.nome_produto = nome_produto
        self.nome_marca = nome_marca
        self.codigo = codigo
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.descricao = descricao
        self.fornecedor = fornecedor

    def __str__(self):
        return (f"Produto: {self.nome_produto} | Marca: {self.nome_marca} | "
                f"Código do produto: {self.codigo} | "
                f"Categoria: {self.categoria} | "
                f"Quantidade em estoque: {self.quantidade} | "
                f"Preço: R${self.preco:,.2f} | "
                f"Descrição: {self.descricao} | "
                f"Fornecedor: {self.fornecedor}")


# ==== Classe Estoque (inalterada) ====
class Estoque:
    def __init__(self):
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
        print("\n=== Produtos em Estoque ===")
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        for produto in self.produtos.values():
            print(produto)
            if produto.quantidade < 5:
                print("Estoque baixo!")

    def buscar_produto(self, codigo):
        return self.produtos.get(codigo, None)

# ==== NOVAS FUNÇÕES DE VALIDAÇÃO COM TRY-EXCEPT ====
def obter_inteiro(mensagem):
    """Pede um número inteiro ao usuário e garante que a entrada seja válida."""
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

def obter_float(mensagem):
    """Pede um número float ao usuário e garante que a entrada seja válida."""
    while True:
        try:
            # Substitui vírgula por ponto para aceitar ambos os formatos (ex: 50,99 e 50.99)
            entrada = input(mensagem).replace(',', '.')
            valor = float(entrada)
            return valor
        except ValueError:
            print("Erro: Por favor, digite um número válido (ex: 50.99).")

# ==== Função de cadastro interativo (ATUALIZADA) ====
def cadastrar_produto_interativo():
    nome_produto = input("Digite o nome do produto: ")
    nome_marca = input("Digite a marca do produto: ")
    codigo = input("Digite o código do produto: ")
    categoria = input("Digite a categoria do produto: ")
    # USA A NOVA FUNÇÃO DE VALIDAÇÃO
    quantidade = obter_inteiro("Digite a quantidade em estoque: ")
    # USA A NOVA FUNÇÃO DE VALIDAÇÃO
    preco = obter_float("Digite o preço do produto: ")
    descricao = input("Digite uma descrição para o produto: ")
    fornecedor = input("Digite o nome do fornecedor: ")

    return Produto(nome_produto, nome_marca, codigo, categoria, quantidade, preco, descricao, fornecedor)


# ==== Programa Principal (ATUALIZADO) ====
if __name__ == "__main__":
    estoque = Estoque()

    while True:
        print("\n=== Sistema de Gestão de Estoque ===")
        print("1 - Cadastrar produto")
        print("2 - Adicionar ao estoque")
        print("3 - Remover do estoque")
        print("4 - Ajustar quantidade em estoque")
        print("5 - Listar produtos")
        print("6 - Buscar produto")
        print("7 - Vendas")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produto = cadastrar_produto_interativo()
            estoque.cadastrar_produto(produto)
        elif opcao == "2":
            codigo = input("Digite o código do produto: ")
            # USA A NOVA FUNÇÃO DE VALIDAÇÃO
            quantidade = obter_inteiro("Digite a quantidade a adicionar: ")
            estoque.adicionar_estoque(codigo, quantidade)
        elif opcao == "3":
            codigo = input("Digite o código do produto: ")
            # USA A NOVA FUNÇÃO DE VALIDAÇÃO
            quantidade = obter_inteiro("Digite a quantidade a remover: ")
            estoque.remover_estoque(codigo, quantidade)
        elif opcao == "4":
            codigo = input("Digite o código do produto: ")
            # USA A NOVA FUNÇÃO DE VALIDAÇÃO
            nova_qtd = obter_inteiro("Digite a nova quantidade: ")
            estoque.ajustar_estoque(codigo, nova_qtd)
        elif opcao == "5":
            estoque.listar_produtos()
        elif opcao == "6":
            codigo = input("Digite o código do produto: ")
            produto = estoque.buscar_produto(codigo)
            print(produto if produto else "Produto não encontrado.")
        elif opcao == "7":
            codigo = input("Digite o código do produto a ser vendido: ")
            produto = estoque.buscar_produto(codigo)
            if produto:
                # USA A NOVA FUNÇÃO DE VALIDAÇÃO
                qtd_venda = obter_inteiro(f"Quantas unidades de '{produto.nome_produto}' deseja vender? ")
                estoque.remover_estoque(codigo, qtd_venda)
            else:
                print("Produto não encontrado.")
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")