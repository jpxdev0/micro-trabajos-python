import random
def factorial(numero):
    if numero <= 1:
        return 1
    return numero * factorial(numero - 1)
n = random.randint(1,10)
print(f"tu numero elegido es {n}")
print(factorial(n))

k = random.randint(10,20)

def calcularPermutaciones(n,k):
    return factorial(n)/factorial(n-k)

def calcularCombinacionees(n,k):
    return factorial(n)/(factorial(n-k)*factorial(k))
print(f"Las permutaciones de {n} en {k} es", calcularPermutaciones(n,k))
print(f"La combinacion de {n} y {k} es: {calcularCombinacionees(n,k)}")


    