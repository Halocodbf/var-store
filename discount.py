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


def aplicar_desconto_interativo(estoque):
    codigo = input("Digite o código do produto para aplicar o desconto: ")
    try:
        percentual = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))
        estoque.aplicar_desconto_produto(codigo, percentual)
    except ValueError:
        print("Valor inválido. O percentual de desconto deve ser um número.")