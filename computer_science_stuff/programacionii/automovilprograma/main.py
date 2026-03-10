from class_automovil import Automovil



mis_100_autos = []


for _ in range(100):
    mis_100_autos.append(Automovil.crea_auto())

print("--- ASÍ SALIERON DE LA FÁBRICA (Desordenados) ---")
for i in range(5):
    print(mis_100_autos[i])


Automovil.ordenar_autos_anio(mis_100_autos, 0, len(mis_100_autos))


print("\n--- LISTA DE 100 AUTOS ORDENADA POR AÑO ---")
for auto in mis_100_autos:
    print(auto)