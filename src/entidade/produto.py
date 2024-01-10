class Produto: #Define uma classe chamada Produto que representa um produto no sistema.
    def __init__(self, nome, preco, estoque):
        #O método especial __init__ é um construtor que é 
        # chamado quando uma instância da classe é criada. 
        # Inicializa os atributos nome, preco e estoque.
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def calcular_desconto(self, quantidade):
        # Lógica para calcular desconto
        return self.preco * quantidade * 0.1  # Desconto de 10%

    def realizar_compra(self, quantidade):
        #Um método que simula a compra do produto. 
        # Verifica se há estoque suficiente.
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            return True
        else:
            return False
