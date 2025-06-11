# Importação das Camadas.
from cliente import Cliente, Clientes
from categoria import Categoria, Categorias
from produto import Produto, Produtos
from venda import Venda, Vendas
from vendaitem import VendaItem, VendaItens

class View:

    # ----------------------------------------
    # Cliente - Operações CRUD
    # ----------------------------------------

    @staticmethod
    def cadastrar_admin():
        # Garante que o cliente 'admin' esteja cadastrado
        for cliente in Clientes.listar():
            if cliente.email == "admin":
                return
        View.cliente_inserir("admin", "admin", "1234")

    @staticmethod
    def cliente_inserir(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        Clientes.inserir(c)

    @staticmethod
    def cliente_listar():
        return Clientes.listar()

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        Clientes.atualizar(c)

    @staticmethod
    def cliente_excluir(id):
        c = Cliente(id, "", "", "")
        Clientes.excluir(c)

    # ----------------------------------------
    # Categoria - Operações CRUD
    # ----------------------------------------

    @staticmethod
    def inserir_categoria(descricao):
        c = Categoria(0, descricao)
        Categorias.inserir(c)

    @staticmethod
    def listar_categorias():
        return Categorias.listar()

    @staticmethod
    def atualizar_categoria(id, descricao):
        c = Categoria(id, descricao)
        Categorias.atualizar(c)

    @staticmethod
    def excluir_categoria(id):
        c = Categoria(id, "")
        Categorias.excluir(c)

    # ----------------------------------------
    # Produto - Operações CRUD
    # ----------------------------------------

    @staticmethod
    def inserir_produto(descricao, preco, estoque, id_categoria):
        p = Produto(0, descricao, preco, estoque)
        p.id_categoria = id_categoria
        Produtos.inserir(p)

    @staticmethod
    def listar_produtos():
        return Produtos.listar()

    @staticmethod
    def atualizar_produto(id, descricao, preco, estoque, id_categoria):
        p = Produto(id, descricao, preco, estoque)
        p.id_categoria = id_categoria
        Produtos.atualizar(p)

    @staticmethod
    def excluir_produto(id):
        p = Produto(id, "", "", "")
        Produtos.excluir(p)

    # ----------------------------------------
    # Venda / Carrinho - Criação e manipulação
    # ----------------------------------------

    @staticmethod
    def inserir_venda():
        # Cria um novo carrinho de compras (venda em aberto)
        v = Venda(0)
        Vendas.inserir(v)
        return v

    @staticmethod
    def listar_vendas_com_itens():
        # Lista todas as vendas com seus respectivos itens formatados
        vendas_formatadas = []
        for v in Vendas.listar():
            venda_info = str(v)
            itens_info = []
            for item in VendaItens.listar():
                if item.id_venda == v.id:
                    id_produto = item.id_produto
                    descricao = Produtos.listar_id(id_produto).descricao
                    itens_info.append(f"  {descricao} - Qtd: {item.qtd} - R$ {item.preco:.2f}")
            vendas_formatadas.append((venda_info, itens_info))
        return vendas_formatadas

    @staticmethod
    def listar_itens_do_carrinho(id_carrinho):
        # Lista os itens de um carrinho específico
        itens_formatados = []
        carrinho = Vendas.listar_id(id_carrinho)
        for item in VendaItens.listar():
            if item.id_venda == id_carrinho:
                produto = Produtos.listar_id(item.id_produto)
                itens_formatados.append(f"  {produto.descricao} - Qtd: {item.qtd} - R$ {item.preco:.2f}")
        return carrinho, itens_formatados

    @staticmethod
    def inserir_produto_no_carrinho(id_carrinho, id_produto, qtd):
        # Adiciona um produto ao carrinho e atualiza o total da venda
        preco = Produtos.listar_id(id_produto).preco
        vi = VendaItem(0, qtd, preco)
        vi.id_venda = id_carrinho
        vi.id_produto = id_produto
        VendaItens.inserir(vi)

        subtotal = qtd * preco
        carrinho = Vendas.listar_id(id_carrinho)
        carrinho.total += subtotal
        Vendas.atualizar(carrinho)

    @staticmethod
    def confirmar_compra(id_carrinho):
        # Finaliza o carrinho e atualiza o estoque dos produtos
        carrinho = Vendas.listar_id(id_carrinho)
        carrinho.carrinho = False
        Vendas.atualizar(carrinho)

        for item in VendaItens.listar():
            if item.id_venda == id_carrinho:
                produto = Produtos.listar_id(item.id_produto)
                produto.estoque -= item.qtd
                Produtos.atualizar(produto)
