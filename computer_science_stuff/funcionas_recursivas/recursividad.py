def sumar_hasta(numero):
    # El freno de mano matemático
    if numero <= 0:
        return 0

    # La recursividad sumando
    return numero + sumar_hasta(numero - 1)

# Como la función ahora DEVUELVE un valor en lugar de imprimirlo, 
# tenemos que ponerla dentro de un print para ver el resultado final
resultado = sumar_hasta(10)
print(f"El total es: {resultado}")