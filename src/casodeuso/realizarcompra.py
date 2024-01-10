class RealizarCompra:
    #que encapsula a lógica para realizar uma compra.
    def __init__(self, produto):
        self.produto = produto

    def executar(self, quantidade):
        # Método que executa a compra,
        #  chamando o método realizar_compra do objeto Produto.
        if self.produto.realizar_compra(quantidade):
            desconto = self.produto.calcular_desconto(quantidade)
            return f"Compra realizada com sucesso! Desconto aplicado: ${desconto}"
        else:
            return "Estoque insuficiente para realizar a compra."
