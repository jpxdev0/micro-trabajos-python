import math
import random
# Importamos NUESTRA clase desde el otro archivo
from mate_prog_func import Funciones

# 1. GENERACIÓN DE NÚMEROS ALEATORIOS
# randint(1, 10) genera enteros: 1, 2, 3...
# uniform(1, 10) genera flotantes: 1.45, 7.89, 3.14...
A = random.randint(1, 10)
B = random.uniform(1, 10)
C = random.uniform(-10, 10)

print("--- VARIABLES ALEATORIAS ---")
# La sintaxis {:.2f} le dice a Python: "Imprime esta variable, pero recórtala a solo 2 decimales"
print(f"A = {A} | B = {B:.2f} | C = {C:.2f}\n")

# 2. INSTANCIACIÓN (Crear el objeto)
# Aquí llamamos al __init__ de la clase. Construimos nuestra "calculadora"
# llamada "mis_funciones" y le metemos los números aleatorios que acabamos de crear.
mis_funciones = Funciones(A, B, C)

# 3. ENTRADA DE DATOS DEL USUARIO
valor_inicial = int(input("Ingrese el valor inicial de x > "))
valor_final = int(input("Ingrese el valor final de x > "))

# 4. EVALUACIÓN USANDO LA FUNCIÓN DE ORDEN SUPERIOR
print("\n--- EVALUANDO EN PUNTO INICIAL (x = {}) ---".format(valor_inicial))

# ¡OJO AQUÍ! Mira cómo usamos funcion_master.
# Primer parámetro: el número a evaluar (valor_inicial).
# Segundo parámetro: EL NOMBRE DE LA FUNCIÓN que queremos usar (mis_funciones.potencia).
# Nota que NO le ponemos paréntesis a .potencia, porque no la estamos ejecutando ahí, 
# se la estamos "pasando" como paquete a funcion_master para que ELLA la ejecute adentro.
print(f"Potencia: {mis_funciones.funcion_master(valor_inicial, mis_funciones.potencia):.4f}")
print(f"Exponencial: {mis_funciones.funcion_master(valor_inicial, mis_funciones.exponencial):.4f}")
print(f"Trigonométrica: {mis_funciones.funcion_master(valor_inicial, mis_funciones.trigonometrica):.4f}")
print(f"Logarítmica: {mis_funciones.funcion_master(valor_inicial, mis_funciones.logaritmica)}")
print(f"Radical: {mis_funciones.funcion_master(valor_inicial, mis_funciones.radical)}")

print("\n--- EVALUANDO EN PUNTO FINAL (x = {}) ---".format(valor_final))
# Repetimos exactamente lo mismo, pero pasándole el "valor_final" en lugar del inicial
print(f"Potencia: {mis_funciones.funcion_master(valor_final, mis_funciones.potencia):.4f}")
print(f"Exponencial: {mis_funciones.funcion_master(valor_final, mis_funciones.exponencial):.4f}")
print(f"Trigonométrica: {mis_funciones.funcion_master(valor_final, mis_funciones.trigonometrica):.4f}")
print(f"Logarítmica: {mis_funciones.funcion_master(valor_final, mis_funciones.logaritmica)}")
print(f"Radical: {mis_funciones.funcion_master(valor_final, mis_funciones.radical)}")

# ==========================================
# EXTRA: CÁLCULO DEL ÁREA DEL TRAPECIO
# ==========================================
print("\n--- CÁLCULO DE ÁREA DE UN TRAPECIO (Básico) ---")
base_mayor = float(input("Ingrese la base mayor > "))
base_menor = float(input("Ingrese la base menor > "))
altura = float(input("Ingrese la altura > "))

# FUNCIONES LAMBDA
# Una función lambda es una función "desechable" de una sola línea. No usa "def" ni "return".
# Estructura:  nombre = lambda parametros : formula_a_ejecutar
# Tu profe pidió usar funciones de orden superior O lambdas. Aquí le demuestras que sabes usar ambas.
calcular_trapecio = lambda B, b, h: ((B + b) * h) / 2

# Ejecutamos la función lambda pasándole los 3 datos que tecleó el usuario
area = calcular_trapecio(base_mayor, base_menor, altura)
print(f"El área del trapecio simple es: {area:.2f}")

import math
import random
from mate_prog_func import Funciones

A = random.randint(1, 10)
B = random.uniform(1, 10)
C = random.uniform(-10, 10)

print(f"Valores generados: A={A}, B={B:.2f}, C={C:.2f}\n")


mis_funciones = Funciones(A, B, C)


valor_inicial = int(input("Ingrese el inicio de la barda (valor inicial x) > "))
valor_final = int(input("Ingrese el fin de la barda (valor final x) > "))
N = int(input("¿En cuántas rebanadas (trapecios) deseas dividirla? (N) > "))


calcular_trapecio = lambda altura1, altura2, ancho: ((altura1 + altura2) * ancho) / 2

print("\n--- CALCULANDO ÁREA DE LA FUNCIÓN POTENCIA ---")

ancho_rebanada = (valor_final - valor_inicial) / N

area_total = 0

x_actual = valor_inicial 

for i in range(N):
    
    x0 = x_actual                  
    x1 = x_actual + ancho_rebanada 
    
  
    altura_izq = mis_funciones.funcion_master(x0, mis_funciones.potencia)
    altura_der = mis_funciones.funcion_master(x1, mis_funciones.potencia)
    
   
    area_rebanada = calcular_trapecio(altura_izq, altura_der, ancho_rebanada)
    

    area_total = area_total + area_rebanada
    
    x_actual = x1 

print(f"El área total bajo la curva de la función potencia es: {area_total:.4f}")