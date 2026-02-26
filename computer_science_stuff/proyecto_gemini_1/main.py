from armas import Arma
from agentes import Agente
Vandal = Arma("Vandal",40)
Phanthom = Arma("Phanthom", 35)

Jett = Agente("Jett", 100)
Phoenix = Agente("Phoenix", 100)
# Equipamos las armas (usamos la variable del agente, un punto, y el método)
Jett.equipar_arma(Vandal)
Phoenix.equipar_arma(Phanthom)

# ¡A disparar! (Llamamos al método y le pasamos al enemigo en el paréntesis)
Jett.disparar_a(Phoenix)
Phoenix.disparar_a(Jett)