# 5) Utilizando a classe Televisão modificada no exercício anterior, crie duas instâncias (objetos), 
# especificando o valor de min e max por nome.

class Televisão:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = min
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        if(self.canal-1 >= self.cmin):
               self.canal -= 1
    def muda_canal_para_cima(self):
        if(self.canal+1 <= self.cmax):
               self.canal += 1

tv=Televisão(min=1, max=20)
print(tv.cmin)
print(tv.cmax)

tv2=Televisão(max=32, min=1)
print(tv2.cmin)
print(tv2.cmax)