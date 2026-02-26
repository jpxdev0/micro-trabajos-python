def fibonacci(numero):
    if numero <= 1:
        return numero
    
    # Aquí está la magia doble: llamada 1 + llamada 2
    return fibonacci(numero - 1) + fibonacci(numero - 2)

print(fibonacci(5))