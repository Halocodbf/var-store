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


# ==== Cadastro ====
def cadastrar_produto():
    nome_produto = input("Digite o nome do produto: ")
    nome_marca = input("Digite a marca do produto: ")
    codigo = input("Digite o código do produto: ")
    categoria = input("Digite a categoria do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    preco = float(input("Digite o preço do produto: "))
    descricao = input("Digite uma descrição para o produto: ")
    fornecedor = input("Digite o nome do fornecedor: ")

    produto = Nome_do_Produto(nome_produto, nome_marca)
    codigo_produto = Codigo_do_Produto(codigo)
    categoria_produto = Categoria(categoria)
    quantidade_estoque = Quantidade_em_Estoque(quantidade)
    preco_produto = Preco(preco)
    descricao_produto = Descricao(descricao)
    fornecedor_produto = Fornecedor(fornecedor)

    print("\n=== Produto Cadastrado ===")
    print(produto.menu_info())
    print(codigo_produto.menu_info())
    print(categoria_produto.menu_info())
    print(quantidade_estoque.menu_info())
    print(preco_produto.menu_info())
    print(descricao_produto.menu_info())
    print(fornecedor_produto.menu_info())


# Executar cadastro
cadastrar_produto()
