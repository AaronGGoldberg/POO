class Item:
    def __init__(self, nomeProduto, qtComprada, precoUnitario):
        self.set_nomeProduto (nomeProduto)
        self.set_qtComprada (qtComprada)
        self.set_precoUnitario (precoUnitario)

    def get_nomeProduto(self):
        return self.__nomeProduto
    def set_nomeProduto(self, nome):
        if type(nome) != str or nome == ' ':
            raise ValueError ('Este nome não pode ser diferente de String ou não pode estar vazio')
        self.__nomeProduto = nome

    def get_qtComprada(self):
        return self.__qtComprada
    def set_qtComprada(self, quantidade):
        if quantidade < 0:
            raise ValueError ('Esta quantidade não pode ser negativa')
        self.__qtComprada = quantidade

    def get_precoUnitario(self):
        return self.__precoUnitario
    def set_precoUnitario(self, preco):
        if preco < 0:
            raise ValueError ('Este preço não pode ser negativo')
        self.__precoUnitario = preco

    def total(self):
        return self.__qtComprada * self.__precoUnitario
    
    def __str__(self):
        return f'O Item de nome: {self.__nomeProduto}, com quantidades {self.__qtComprada}, de preço {self.__precoUnitario} tem o total de R${self.total()}'