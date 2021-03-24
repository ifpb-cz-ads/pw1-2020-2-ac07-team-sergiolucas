# 2° Atualmente, a classe Televisão inicializa o canal com 2. 
# Modifique a classe Televisão de forma a receber o canal inicial em seu construtor.

# class Televisão:
#      def __init__(self):
#            self.ligada = False
#            self.canal = 2
#      def muda_canal_para_baixo(self):
#            self.canal -= 1
#      def muda_canal_para_cima(self):
#            self.canal += 1

# tv = Televisão()
# tv.muda_canal_para_cima()
# tv.muda_canal_para_cima()
# print(tv.canal)
# tv.muda_canal_para_baixo()
# print(tv.canal)


class Televisão:
     def __init__(self, canal_inicial):
         self.ligada = False
         self.canal = canal_inicial
     def muda_canal_para_baixo(self):
           self.canal -= 1
     def muda_canal_para_cima(self):
           self.canal += 1

tv=Televisão(5)
print(tv.canal)