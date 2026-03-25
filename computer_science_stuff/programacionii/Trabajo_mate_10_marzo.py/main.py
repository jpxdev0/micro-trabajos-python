import math
import random
from mate_prog_func import Funciones, Punto, Figuras

def imprimir_formateado(nombre_funcion, resultado):
    """Evita errores al imprimir textos como 'Indefinido' con formato de número"""
    if isinstance(resultado, str):
        print(f"{nombre_funcion}: {resultado}")
    else:
        print(f"{nombre_funcion}: {resultado:.4f}")

if __name__ == "__main__":
    
    # --- 1. VARIABLES ALEATORIAS ---
    A = random.randint(1, 10)
    B = random.uniform(1, 10)
    C = random.uniform(-10, 10)

    print("--- VARIABLES ALEATORIAS ---")
    print(f"A = {A} | B = {B:.2f} | C = {C:.2f}\n")

    mis_funciones = Funciones(A, B, C)

    diccionario_funciones = {
        "Potencia": mis_funciones.potencia,
        "Exponencial": mis_funciones.exponencial,
        "Trigonométrica": mis_funciones.trigonometrica,
        "Logarítmica": mis_funciones.logaritmica,
        "Radical": mis_funciones.radical
    }

    # --- 2. PUNTOS INICIAL Y FINAL ---
    try:
        x0 = float(input("Ingrese el valor inicial de x (x0) > "))
        x1 = float(input("Ingrese el valor final de x (x1) > "))
    except ValueError:
        print("Error: Ingrese números válidos. Usando 1.0 y 5.0 por defecto.")
        x0, x1 = 1.0, 5.0

    print(f"\n--- EVALUANDO EN PUNTO INICIAL (x0 = {x0}) ---")
    for nombre, func in diccionario_funciones.items():
        imprimir_formateado(nombre, mis_funciones.funcion_master(x0, func))

    print(f"\n--- EVALUANDO EN PUNTO FINAL (x1 = {x1}) ---")
    for nombre, func in diccionario_funciones.items():
        imprimir_formateado(nombre, mis_funciones.funcion_master(x1, func))


    print("\n--- CALCULO DE ÁREA (1 SOLO TRAPECIO ENTRE x0 y x1) ---")
    
    ancho_total = abs(x1 - x0)
    calcular_trapecio_lambda = lambda y_izq, y_der, base: ((y_izq + y_der) * base) / 2

    for nombre, func in diccionario_funciones.items():
        y0 = mis_funciones.funcion_master(x0, func)
        y1 = mis_funciones.funcion_master(x1, func)
        
        if isinstance(y0, str) or isinstance(y1, str):
            print(f"{nombre}: Indefinido (No se puede formar el trapecio)")
        else:
            area_unica = calcular_trapecio_lambda(y0, y1, ancho_total)
            print(f"{nombre}: {area_unica:.4f} unidades cuadradas")


    print("\n--- AREA APROXIMADA DIVIDIDA EN N TRAPECIOS ---")
    try:
        N = int(input("¿En cuantas sub-divisiones (N) desea calcular el área? > "))
    except ValueError:
        print("Usando N=10 por defecto.")
        N = 10

    if N > 0:
        ancho_rebanada = ancho_total / N
        
        lista_puntos_x = []
        for i in range(N + 1):
            punto = x0 + (i * ancho_rebanada)
            lista_puntos_x.append(punto)
            
        print(f"\nLista de {len(lista_puntos_x)} puntos 'x' generados:")
        print([round(p, 2) for p in lista_puntos_x])
        print("\nCalculando suma de áreas...")

        for nombre, func in diccionario_funciones.items():
            area_total = 0
            es_valido = True
            
            for i in range(len(lista_puntos_x) - 1):
                x_act = lista_puntos_x[i]
                x_sig = lista_puntos_x[i + 1]
                
                y_act = mis_funciones.funcion_master(x_act, func)
                y_sig = mis_funciones.funcion_master(x_sig, func)
                
                if isinstance(y_act, str) or isinstance(y_sig, str):
                    es_valido = False
                    break
                
                area_rebanada = calcular_trapecio_lambda(y_act, y_sig, ancho_rebanada)
                area_total += area_rebanada
                
            if es_valido:
                print(f"Area total ({nombre}): {area_total:.4f}")
            else:
                print(f"Area total ({nombre}): Indefinida en este intervalo.")
    else:
        print("El número de trapecios debe ser mayor a 0.")

    print("\n------------------ CLASIFICADOR AUTOMÁTICO DE CUADRILÁTEROS -----------------")
    coordenadas_azar = []
    for _ in range(4):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        coordenadas_azar.append((x, y))
        
    cx = sum(coord[0] for coord in coordenadas_azar) / 4
    cy = sum(coord[1] for coord in coordenadas_azar) / 4
    coord_ordenadas = sorted(coordenadas_azar, key=lambda c: math.atan2(c[1] - cy, c[0] - cx))

    esquina1 = Punto(coord_ordenadas[0][0], coord_ordenadas[0][1])
    esquina2 = Punto(coord_ordenadas[1][0], coord_ordenadas[1][1])
    esquina3 = Punto(coord_ordenadas[2][0], coord_ordenadas[2][1])
    esquina4 = Punto(coord_ordenadas[3][0], coord_ordenadas[3][1])

    print("Esquinas ordenadas generadas:")
    print(f"P1: ({esquina1.x}, {esquina1.y})")
    print(f"P2: ({esquina2.x}, {esquina2.y})")
    print(f"P3: ({esquina3.x}, {esquina3.y})")
    print(f"P4: ({esquina4.x}, {esquina4.y})")

    mi_figura = Figuras(esquina1, esquina2, esquina3, esquina4)
    resultado = mi_figura.clasificar_figura()

    print(f"\n-> ¡La figura resultante es un: {resultado.upper()}! <-")