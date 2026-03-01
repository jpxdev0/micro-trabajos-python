from class_automovil import Automovil


# 1. Creamos nuestra lista vacía
mis_100_autos = []

# 2. Generamos los 100 autos aleatorios usando tu método de clase
for _ in range(100):
    mis_100_autos.append(Automovil.crea_auto())

print("--- ASÍ SALIERON DE LA FÁBRICA (Desordenados) ---")
# Imprimimos solo los primeros 5 para no llenar toda la pantalla de golpe
for i in range(5):
    print(mis_100_autos[i])

# 3. ¡Activamos tu algoritmo de ordenamiento!
# Le pasamos la lista, el inicio (posición 0) y el final (posición 100)
Automovil.ordenar_autos_anio(mis_100_autos, 0, len(mis_100_autos))

# 4. Comprobamos la magia imprimiendo toda la lista ya ordenada
print("\n--- LISTA DE 100 AUTOS ORDENADA POR AÑO ---")
for auto in mis_100_autos:
    print(auto)