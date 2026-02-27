from dig_dif_class import NumeroRaro, dar_bienvenida, Usuario

nombre_usuario = input("Ingrese su nombre: ")
dar_bienvenida(nombre_usuario)

usuario = Usuario(nombre_usuario)
longitud = usuario.pedir_longitud()

numero_raro = NumeroRaro(longitud)
numero_generado = numero_raro.generar_valor()

print(f"Longitud del numero: {longitud}")
print(f"Numero generado al azar: {numero_generado}")
print(f"Digitos: {numero_raro.digitos}")