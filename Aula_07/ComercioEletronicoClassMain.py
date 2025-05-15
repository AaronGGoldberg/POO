import ComercioEletronico
from ComercioEletronicoClassCarinho import Carrinho
from ComercioEletronico import Item
from datetime import datetime

carrinho = Carrinho('Yuri', datetime.now())

item1 = Item('Banana', 5, 50.00)
item2 = Item('Maça', 2, 100.00)
item3 = Item('Mercado', 1, 10.00)

carrinho.inserir(item1)
carrinho.inserir(item2)
carrinho.inserir(item3)

carrinho.remover(item3)

print(f'Itens no carrinho: {carrinho.get_lista()}Com o valor total de: {carrinho.total_lista()}')
print(f'Os dados do carrinho são: {carrinho.__str__()}')