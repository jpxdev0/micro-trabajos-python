import math
import random
from mate_prog_func import Funciones

A = random.randint(1, 10)
B = random.uniform(1, 10)
C = random.uniform(-10, 10)


print(f"A = {A} | B = {B:.2f} | C = {C:.2f}\n")


mis_funciones = Funciones(A, B, C)


valor_inicial = int(input("Ingrese el valor inicial de x > "))
valor_final = int(input("Ingrese el valor final de x > "))


print(f"Potencia: {mis_funciones.funcion_master(valor_inicial, mis_funciones.potencia):.4f}")
print(f"Exponencial: {mis_funciones.funcion_master(valor_inicial, mis_funciones.exponencial):.4f}")
print(f"Trigonometrica: {mis_funciones.funcion_master(valor_inicial, mis_funciones.trigonometrica):.4f}")
print(f"Logaritmica: {mis_funciones.funcion_master(valor_inicial, mis_funciones.logaritmica)}")
print(f"Radical: {mis_funciones.funcion_master(valor_inicial, mis_funciones.radical)}")


print(f"Potencia: {mis_funciones.funcion_master(valor_final, mis_funciones.potencia):.4f}")
print(f"Exponencial: {mis_funciones.funcion_master(valor_final, mis_funciones.exponencial):.4f}")
print(f"Trigonometrica: {mis_funciones.funcion_master(valor_final, mis_funciones.trigonometrica):.4f}")
print(f"Logaritmica: {mis_funciones.funcion_master(valor_final, mis_funciones.logaritmica)}")
print(f"Radical: {mis_funciones.funcion_master(valor_final, mis_funciones.radical)}")



base_mayor = float(input("Ingrese la base mayor > "))
base_menor = float(input("Ingrese la base menor > "))
altura = float(input("Ingrese la altura > "))

calcular_trapecio = lambda B, b, h: ((B + b) * h) / 2

area = calcular_trapecio(base_mayor, base_menor, altura)
print(f"El área del trapecio es: {area:.2f}")