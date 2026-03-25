# 1. Primero definimos nuestra funcion recursiva (la herramienta)
def numeros_primos(n,div=2):
    #paso base, que lo que hace es si nuestro stack(pila) baje hasta 1 
    if n <= 1:
        return 1
   # caso recursivo a (encontramos un primo):
    # agarramos el numero n y lo dividimos usando mod (%) para ver cuanto sobra.
    # Si el sobrante es exactamente 0 significa que la división fue correcta.
    # imprimimos ese divisor, hacemos el número más chiquito (nuevo_numero) 
    # y la función se vuelve a llamar a si misma(iterando esta) usando ese numero nuevo.
    if n % div == 0:
        print(div)
        nuevo_numero = n//div
        numeros_primos(nuevo_numero,div)
    else:
        #si no da 0 aumentamos el divisor hasta que de 0

        div = div+1
        numeros_primos(n,div)
print("----"*30)
print("DESARMADOR DE NUMERO PRIMOS")
print("----"*30)
numero_elegido = int(input("Ingresa un numero para sacar sus factores primos> "))
print(f"Los numeros de los factores primos de {numero_elegido} es:...")
numeros_primos(numero_elegido)

    #un numero primo es aquel que se puede dividir entre 1 y si mismo
    #es decir este numero no puede tener mas divisor mas que el y si mismo
    #ejemplo tenemos un 6, 6 puede tener mas divisores que el y el uno seria dos su divisor mas cercano,
    #el 7 en cambio no seria el y si mismo

    
    
  