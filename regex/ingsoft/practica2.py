from bs4 import BeautifulSoup

html_tienda = """
<html>
  <body>
    <div class="producto">
      <h2 class="titulo">Balatro (PC)</h2>
      <span class="precio">$15.00</span>
    </div>
    <div class="producto">
      <h2 class="titulo">Valorant - 1000 VP</h2>
      <span class="precio">$9.99</span>
    </div>
    <div class="producto">
      <h2 class="titulo">Hollow Knight</h2>
      <span class="precio">$7.50</span>
    </div>
  </body>
</html>
"""

sopa = BeautifulSoup(html_tienda, "html.parser")

# 1. Buscamos todas las CAJAS GRANDES que contienen cada juego
cajas_productos = sopa.find_all("div", class_="producto")

print("Reporte de Ofertas Listo:")

# 2. Recorremos caja por caja
for caja in cajas_productos:
    # Como 'caja' ya es un mini-objeto BeautifulSoup, podemos hacer un .find() dentro de ella
    titulo = caja.find("h2", class_="titulo").text
    
    # TU MISIÓN: Extrae el texto del precio usando caja.find()
    precio = caja.find("span", class_="precio").text
    
    
    # Imprimimos el resultado ensamblado
    print(f"-> El juego {titulo} tiene un costo de {precio}")
    