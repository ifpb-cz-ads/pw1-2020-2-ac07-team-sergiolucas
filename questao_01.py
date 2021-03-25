# 1) Adicione os atributos tamanho e marca à classe Televisão. Crie dois objetos Televisão e
# atribua tamanhos e marcas diferentes. Depois, imprima o valor desses atributos de forma a
# confirmar a independência dos valores de cada instância (objeto).

class Televisão:
    def __init__(self):
        self.tamanho = None
        self.marca = None
        self.ligada = False
        self.canal = None

tv1 = Televisão()
tv2 = Televisão()

tv1.marca = 'Samsung'
tv1.tamanho = 32
tv1.ligada = False
tv1.canal = 0

tv2.marca = 'Sony'
tv2.tamanho = 14
tv2.ligada = True
tv2.canal = 6

print(f' Marca: {tv1.marca} ' + f'Tamanho: {tv1.tamanho} ' + f'Ligada: {tv1.ligada} ' + f'Canal: {tv1.canal}')
print(f' Marca: {tv2.marca} ' + f'Tamanho: {tv2.tamanho} ' + f'Ligada: {tv2.ligada} ' + f'Canal: {tv2.canal}')
