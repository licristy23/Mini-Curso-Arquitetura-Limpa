
from entidade.produto import Produto
from casodeuso.realizarcompra import RealizarCompra
from adaptadoresdeinteface.adaptadorcompraweb import AdaptadorCompraWeb
def main():
    produto_e_commerce = Produto("Camiseta", 25.0, 100)
    caso_uso_compra = RealizarCompra(produto_e_commerce)
    adaptador_web = AdaptadorCompraWeb(produto_e_commerce)

    # Simulação de compra via formulário web
    dados_entrada_web = {'quantidade': 5}
    quantidade_compra = adaptador_web.converter_dados_entrada(dados_entrada_web)
    resultado_compra = caso_uso_compra.executar(quantidade_compra)
    resposta_web = adaptador_web.converter_dados_saida(resultado_compra)

    print(resposta_web)

# Chamada da Função Main
if __name__ == "__main__":
    main()
