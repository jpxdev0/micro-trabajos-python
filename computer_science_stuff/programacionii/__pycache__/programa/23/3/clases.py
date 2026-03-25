sueldo= {
    "Tiempo completo":{
        "Asistente": 16658.39,
        "AsociadoA": 18682.54,

    },
    "Medio tiempo":{
        "Asociado A": 9342.75,
        "Asociado B": 10474.58,
        "Asociado C":  11378.36,
    },
    "Tecnicos Academicos":{
        "Basico": 15901.58,
        "General A": 17809.21
    },
    "Horas Sueltas":{
        "Categoria A": 486.00,
        "Categoria B anterior": 564.58
    }
}
# Iniciando main
print("Que categoria pertenece? ")
repuesta = input("")                   
#Preguntar si la respuesta esta en el diccionario
if repuesta in sueldo:
   nivel = input("A que nivel pertenece> ")
   if nivel in sueldo[respuesta]:
       if respuesta == "Horas Sueltas":
           hora = int(input("Horas trabajadas> "))
       print(f"sueldo[respuesta][nivel]")

else:
    print("Escribalo bien alv")
