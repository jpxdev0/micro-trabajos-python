import re

# 1. Los datos del corte de caja (el desastre del contador)
registro_ventas = """
Mesa 1: Tacos al pastor ... $15.50 (pagado)
Mesa 2: Refresco de dieta ... $2.00
Mesa 3: Orden de guacamole - 80 pesos (pendiente)
Mesa 4: Propina sugerida: $5.00
Mesa 5: Corte de carne premium $120.99 // VIP
Mesa 6: Mesa rota, cobro de penalización: $500.00
"""

# 2. TU MISIÓN: Define el patrón para atrapar los precios con formato $XX.XX
# REGLA DE ORO: El símbolo de dólar ($) también es un "comodín mágico" en Regex (significa final de línea). 
# ¿Recuerdas cómo le quitaste la magia al punto en el ejercicio pasado? Aquí harás lo mismo.
patron_dinero = r"[\$]+\d+[\.]+\d+"

# 3. Ejecutamos la búsqueda
precios_encontrados = re.findall(patron_dinero, registro_ventas)

# 4. Mostramos el resultado
print("Precios extraídos para el contador:")
for precio in precios_encontrados:
    print(f"-> {precio}")