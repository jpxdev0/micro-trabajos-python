class Agente:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        self.arma_equipada = None

        
    def equipar_arma(self, arma_nueva):
        self.arma_equipada = arma_nueva
        print (f"{self.nombre}. ha equipado un nuevo arma")
        print (f"{self.nombre} ha equipado el arma {arma_nueva.nombre}")
        
    def recibir_danio(self, cantidad):
        self.vida = self.vida - cantidad
        print(f"{self.nombre},recibio{cantidad}, de danio, {self.vida}, restante")

    def disparar_a(self, enemigo):
        if self.arma_equipada == None: # <- Faltaban los dos puntos
            return
            
        dano_arma = self.arma_equipada.dano
        
        # Le pasamos la variable normal, sin el self, a la función con el nombre exacto
        enemigo.recibir_danio(dano_arma)
