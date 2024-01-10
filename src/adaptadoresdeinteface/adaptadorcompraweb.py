class AdaptadorCompraWeb:
    def __init__(self, produto):
        self.produto = produto

    def converter_dados_entrada(self, dados_entrada_web):
        # Lógica para converter dados de entrada do formulário web
        return dados_entrada_web['quantidade']

    def converter_dados_saida(self, resultado_compra):
        # Lógica para converter dados de saída para exibição web ou resposta de API
        return {"mensagem": resultado_compra}