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


# ==== Cadastro ====
def cadastrar_produto():
    nome_produto = input("Digite o nome do produto: ")
    nome_marca = input("Digite a marca do produto: ")
    codigo = input("Digite o código do produto: ")
    categoria = input("Digite a categoria do produto: ")

    produto = Nome_do_Produto(nome_produto, nome_marca)
    codigo_produto = Codigo_do_Produto(codigo)
    categoria_produto = Categoria(categoria)

    print("\n=== Produto Cadastrado ===")
    print(produto.menu_info())
    print(codigo_produto.menu_info())
    print(categoria_produto.menu_info())


# Executar cadastro
cadastrar_produto()
