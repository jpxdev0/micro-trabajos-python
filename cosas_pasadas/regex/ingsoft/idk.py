from bs4 import BeautifulSoup

# 1. El código de la página web (súper simple)
mi_pagina = """
<html>
    <div class="saludo">Hola Mundo</div>
    <div class="despedida">Adios</div>
</html>
"""

# 2. Convertimos el texto en un Objeto de Python
sopa = BeautifulSoup(mi_pagina, "html.parser")

# 3. Usamos el método .find() del objeto para buscar nuestra caja
# Le decimos: "Búscame la etiqueta 'div' que tenga la clase 'saludo'"
mi_caja = sopa.find("div", class_="saludo")

# 4. Si imprimimos mi_caja, nos da toda la etiqueta: <div class="saludo">Hola Mundo</div>
# Pero si usamos la propiedad .text, nos da SOLO lo de adentro
print(mi_caja.text)