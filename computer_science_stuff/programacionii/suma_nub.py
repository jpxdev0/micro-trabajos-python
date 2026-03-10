def suma_natural(inicio,fin):
    #retornar la suma fin signo de suma abajo k= inicio
    # TODO: pedir inicio y fin al usuario
    suma = 0 
    for i in range(inicio,fin+1):
        suma += i 
    return suma
inicio = int(input("ingresa el inicio> "))
final = int(input("ingresa el final> "))
print(suma_natural(inicio,final))

def suma_cubo(inicio, fin):
    suma = 0
    for k in range(inicio, fin + 1):
        suma += k**3
    return suma

print(suma_cubo(inicio, final))
