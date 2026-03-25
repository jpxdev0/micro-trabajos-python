class Sumador:
    @staticmethod
    def suma(inicio,final, termino):
        res = 0
        while inicio!= final + 1:
            res = res + termino(inicio)
            inicio += 1
        return res
    @staticmethod
    def natural(x):
        return x
    @staticmethod
    def cubo(x):
        return x*x*x
    @staticmethod
    def divPar(x):
        return(1/(x*2))
print(Sumador.suma(3,5,Sumador.natural))
print(Sumador.suma(3,5,Sumador.cubo))
print(Sumador.suma(3,5,Sumador.divPar))
s = Sumador()
print(s.suma(3,5,s.natural))
