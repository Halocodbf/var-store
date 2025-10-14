from operacoes_venda import OperacoesVenda
from discount import Preco, aplicar_desconto_interativo
from relatorio import RegistroVendas
from movimentacao import registrar_movimento, relatorio_estoque, historico_movimentos

# ==== Classe Produto ====
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
                f"Código: {self.codigo} | Categoria: {self.categoria} | "
                f"Quantidade: {self.quantidade} | {self.preco.menu_info()} | " # LINHA MODIFICADA
                f"Descrição: {self.descricao} | Fornecedor: {self.fornecedor}")


# ==== Classe Estoque ====
class Estoque:
    def __init__(self):
        self.produtos = {}

    def cadastrar_produto(self, produto):
        if produto.codigo in self.produtos:
            print("Produto com este código já existe.")
        else:
            self.produtos[produto.codigo] = produto
            registrar_movimento(produto.nome_produto, produto.quantidade, "Cadastro")
            print("Produto cadastrado com sucesso!")

    def adicionar_estoque(self, codigo, quantidade):
        if codigo in self.produtos:
            self.produtos[codigo].quantidade += quantidade
            registrar_movimento(self.produtos[codigo].nome_produto, quantidade, "Entrada")
            print("Estoque atualizado.")
        else:
            print("Produto não encontrado.")

    def remover_estoque(self, codigo, quantidade):
        if codigo in self.produtos:
            if self.produtos[codigo].quantidade >= quantidade:
                self.produtos[codigo].quantidade -= quantidade
                registrar_movimento(self.produtos[codigo].nome_produto, quantidade, "Saída")
                print("Quantidade removida do estoque.")
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Produto não encontrado.")

    def ajustar_estoque(self, codigo, nova_quantidade):
        if codigo in self.produtos:
            diferenca = nova_quantidade - self.produtos[codigo].quantidade
            tipo = "Ajuste (+)" if diferenca > 0 else "Ajuste (-)"
            self.produtos[codigo].quantidade = nova_quantidade
            registrar_movimento(self.produtos[codigo].nome_produto, abs(diferenca), tipo)
            print("Estoque ajustado.")
        else:
            print("Produto não encontrado.")

    def listar_produtos(self):
        print("\n=== Produtos em Estoque ===")
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return
        for produto in self.produtos.values():
            print(produto)
            if produto.quantidade < 5:
                print("Estoque baixo!")

    def buscar_produto(self, codigo):
        return self.produtos.get(codigo, None)
    
    def aplicar_desconto_produto(self, codigo, percentual):
        produto = self.buscar_produto(codigo)
        if produto:
            produto.preco.aplicar_desconto(percentual)
        else:
            print("Produto não encontrado.")


# ==== Funções auxiliares ====
def obter_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

def obter_float(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Erro: Digite um número válido (ex: 49.90).")

def cadastrar_produto_interativo():
    print("\n=== Cadastro de Produto ===")
    nome_produto = input("Nome do produto: ")
    nome_marca = input("Marca: ")
    codigo = input("Código: ")
    categoria = input("Categoria: ")
    quantidade = obter_inteiro("Quantidade inicial: ")
    preco_valor = obter_float("Preço do produto (R$): ")
    preco_objeto = Preco(preco_valor)
    descricao = input("Descrição: ")
    fornecedor = input("Fornecedor: ")
    return Produto(nome_produto, nome_marca, codigo, categoria, quantidade, preco_objeto, descricao, fornecedor)


# ==== Programa Principal ====
if __name__ == "__main__":
    estoque = Estoque()
    registro_vendas = RegistroVendas()
    operacoes = OperacoesVenda(estoque)

    while True:
        print("\n=== Sistema de Gestão de Varejo ===")
        print("1 - Cadastrar produto")
        print("2 - Adicionar estoque")
        print("3 - Remover estoque")
        print("4 - Ajustar quantidade")
        print("5 - Listar produtos")
        print("6 - Buscar produto")
        print("7 - Registrar venda")
        print("8 - Aplicar desconto")
        print("9 - Histórico de movimentações")
        print("10 - Relatório de vendas")
        print("11 - Relatório de Estoque (simplificado)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produto = cadastrar_produto_interativo()
            estoque.cadastrar_produto(produto)

        elif opcao == "2":
            codigo = input("Código do produto: ")
            qtd = obter_inteiro("Quantidade a adicionar: ")
            estoque.adicionar_estoque(codigo, qtd)

        elif opcao == "3":
            codigo = input("Código do produto: ")
            qtd = obter_inteiro("Quantidade a remover: ")
            estoque.remover_estoque(codigo, qtd)

        elif opcao == "4":
            codigo = input("Código do produto: ")
            nova_qtd = obter_inteiro("Nova quantidade: ")
            estoque.ajustar_estoque(codigo, nova_qtd)

        elif opcao == "5":
            estoque.listar_produtos()

        elif opcao == "6":
            codigo = input("Código do produto: ")
            produto = estoque.buscar_produto(codigo)
            print(produto if produto else "Produto não encontrado.")

        elif opcao == "7":
            operacoes.registrar_venda()
            registro_vendas.registrar_venda("Venda registrada via OperacoesVenda")

        elif opcao == "8":
            aplicar_desconto_interativo(estoque)

        elif opcao == "9":
            historico_movimentos()

        elif opcao == "10":
            registro_vendas.gerar_relatorio()
        
        elif opcao == "11":
            relatorio_estoque(estoque)

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")
