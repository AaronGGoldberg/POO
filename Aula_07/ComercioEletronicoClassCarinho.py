from datetime import datetime
from ComercioEletronico import Item

class Carrinho:
    def __init__(self, nomeCliente, dataPedido):
        self.set_nomeCliente(nomeCliente)
        self.set_dataPedido(dataPedido)
        self.__listaItens = []

    def get_nomeCliente(self):
        return self.__nomeCliente
    def set_nomeCliente(self, nome):
        if nome == " " or type(nome) != str:
            raise ValueError ('Este nome não pode ser vazio e nem ser diferente de String')
        self.__nomeCliente = nome

    def get_dataPedido(self):
        return self.__dataPedido
    def set_dataPedido(self, data):
        if data > datetime.now():
            raise ValueError ('Esta data não pode estar no futuro')
        self.__dataPedido = data
    def get_lista(self):
        s = ""
        for item in self.__listaItens:
            s += item.__str__()
            s += " ,"
        return s
    def inserir(self, item):
        if type(item) != Item:
            raise ValueError('Este Item não existe')
        self.__listaItens.append(item)
    def remover(self, item):
        if type(item) != Item or item == " ":
            raise ValueError('Este Item não existe')
        self.__listaItens.remove(item)

    def total_lista(self):
        cont = 0
        for item in self.__listaItens:
            item.total() 
            cont += item.total()
        return cont    

    def __str__(self):
        return f'Carrinho do Cliente: {self.__nomeCliente}, na Data: {self.__dataPedido.strftime("%d/%m/%Y")}, existem {len(self.__listaItens)} Itens, com um total de R$ {self.total_lista()}' 