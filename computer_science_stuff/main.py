class AgenteValorant:
    def __init__(self, nombre, vida): # Solo nace con nombre y vida
        self.nombre = nombre
        self.vida = vida

    def recibir_disparo(self, dano):
        self.vida = self.vida - dano
        print(f"¡{self.nombre} recibió {dano} de daño! Vida restante: {self.vida}")

    def disparar_a(self, enemigo): # Aquí recibimos al objetivo en el momento
        print(f"{self.nombre} está disparando con una Vandal...")
        
        # ¡LA LÍNEA MÁGICA!
        # Le decimos a ese objeto 'enemigo' que ejecute su propia función de recibir daño:
        enemigo.recibir_disparo(40)

# Creamos a los agentes
jett = AgenteValorant("Jett", 100)
phoenix = AgenteValorant("Phoenix", 100)

# Jett le dispara a Phoenix
jett.disparar_a(phoenix)