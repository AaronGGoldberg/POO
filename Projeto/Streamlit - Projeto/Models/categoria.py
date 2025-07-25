import json
from Models.modelo import Modelo

class Categoria:
    def __init__(self, id, descricao):
        self.setId(id)       
        self.setDescricao(descricao)
    def __str__(self):
        return f"{self.getId()} - {self.getDescricao()}"

    def getId(self):
        return self.__id 
    
    def setId(self, id):
        if id < 0:
            raise ValueError("O ID não pode ser negativo.")
        self.__id = id

    def getDescricao(self):
        return self.__descricao
    
    def setDescricao(self, descricao):
        if descricao == "" or descricao is None:
            raise ValueError("A descrição não pode ser vazia.")
        self.__descricao = descricao


class Categorias(Modelo):    # Persistência - Armazena os objetos em um arquivo/banco de dados
    @classmethod
    def abrir(cls):
        cls.objetos = [] 
        try:    
            with open("categorias.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Categoria(dic["_Categoria__id"], dic["_Categoria__descricao"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    