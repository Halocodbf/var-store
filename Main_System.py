# ==== Classes de atributos ====
class Nome_do_Produto:
    def __init__(self, nome_produto, nome_marca):
        self.nome_produto = nome_produto
        self.nome_marca = nome_marca

    def menu_info(self):
        return f"Produto: {self.nome_produto} | Marca: {self.nome_marca}"


class Codigo_do_Produto:
    def __init__(self, codigo):
        self.codigo = codigo

    def menu_info(self):
        return f"Código do produto: {self.codigo}"


class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

    def menu_info(self):
        return f"Categoria: {self.categoria}"


class Quantidade_em_Estoque:
    def __init__(self, quantidade):
        self.quantidade = quantidade

    def menu_info(self):
        return f"Quantidade em estoque: {self.quantidade}"


class Preco:
    def __init__(self, preco):
        self.preco = preco

    def menu_info(self):
        return f"Preço: R${self.preco:,.2f}"


class Descricao:
    def __init__(self, descricao):
        self.descricao = descricao

    def menu_info(self):
        return f"Descrição: {self.descricao}"


class Fornecedor:
    def __init__(self, fornecedor):
        self.fornecedor = fornecedor

    def menu_info(self):
        return f"Fornecedor: {self.fornecedor}"


# ==== Classe Produto (composta pelas outras classes) ====
class Produto:
    def __init__(self, nome_produto, nome_marca, codigo, categoria, quantidade, preco, descricao, fornecedor):
        self.nome = Nome_do_Produto(nome_produto, nome_marca)
        self.codigo = Codigo_do_Produto(codigo)
        self.categoria = Categoria(categoria)
        self.quantidade = Quantidade_em_Estoque(quantidade)
        self.preco = Preco(preco)
        self.descricao = Descricao(descricao)
        self.fornecedor = Fornecedor(fornecedor)

    def __str__(self):
        return (f"{self.nome.menu_info()} | {self.codigo.menu_info()} | "
                f"{self.categoria.menu_info()} | {self.quantidade.menu_info()} | "
                f"{self.preco.menu_info()} | {self.descricao.menu_info()} | "
                f"{self.fornecedor.menu_info()}")


# ==== Classe Estoque ====
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
                print("Quantidade removida do estoque.")
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Produto não encontrado.")

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


# ==== Função de cadastro interativo ====
def cadastrar_produto():
    nome_produto = input("Digite o nome do produto: ")
    nome_marca = input("Digite a marca do produto: ")
    codigo = input("Digite o código do produto: ")
    categoria = input("Digite a categoria do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    preco = float(input("Digite o preço do produto: "))
    descricao = input("Digite uma descrição para o produto: ")
    fornecedor = input("Digite o nome do fornecedor: ")

    return Produto(nome_produto, nome_marca, codigo, categoria, quantidade, preco, descricao, fornecedor)


# ==== Programa Principal ====
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
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produto = cadastrar_produto()
            estoque.cadastrar_produto(produto)
        elif opcao == "2":
            codigo = input("Digite o código do produto: ")
            quantidade = int(input("Digite a quantidade a adicionar: "))
            estoque.adicionar_estoque(codigo, quantidade)
        elif opcao == "3":
            codigo = input("Digite o código do produto: ")
            quantidade = int(input("Digite a quantidade a remover: "))
            estoque.remover_estoque(codigo, quantidade)
        elif opcao == "4":
            codigo = input("Digite o código do produto: ")
            nova_qtd = int(input("Digite a nova quantidade: "))
            estoque.ajustar_estoque(codigo, nova_qtd)
        elif opcao == "5":
            estoque.listar_produtos()
        elif opcao == "6":
            codigo = input("Digite o código do produto: ")
            produto = estoque.buscar_produto(codigo)
            print(produto if produto else "❌ Produto não encontrado.")
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
