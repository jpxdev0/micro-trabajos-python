import random
class Automovil:
   
    #modelo pendiente
    #anio = [2020,2021,2026]
    anio = range(2020,2027)
    diccionario = {"Toyota":["Corola","camry","prius"],
                   "Ford": ["Lobo","f-150","Explorador"],
                   "Dodge": ["charger", "Durango", "ram"],
                   "Honda":["civic","accord","crv"],
                    "Chevrolet": ["impala","malibu", "silverado"],
                    "Nissan":["altima","sentra","rougue"],
                    "Mazda": ["X7", "3", "5"]}
    def __init__(self,marca = 'honda', modelo = 'civic', anio = '2021'):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    @classmethod
    def crea_auto(cls):
        marca = random.choice(list(Automovil.diccionario.keys()))
        modelo = random.choice(Automovil.diccionario[marca])
        anio = random.choice(Automovil.anio)
        return  Automovil(marca, modelo, anio)
    def __str__(self):
        return f"Soy un {self.marca} {self.modelo} del anio {self.anio}"
    def __lt__(self, other):
        return self.anio< other.anio
    def __gt__(self, other):
        return self.anio > other.anio
    @staticmethod
    def fusionar(lista, o, mitad, i):
        # 1. Copiamos las dos mitades (nuestras dos filas de jugadores)
        izquierda = lista[o:mitad]
        derecha = lista[mitad:i]
        
        # 2. Creamos una lista nueva y vacía, justo como lo hiciste en tu main
        lista_ordenada = []
        
        # 3. Mientras haya jugadores en AMBAS filas, los ponemos a competir
        while len(izquierda) > 0 and len(derecha) > 0:
            
            # Comparamos al primero de cada fila
            if izquierda[0] < derecha[0]:
                # Gana el de la izquierda. Lo sacamos de su fila con pop(0) 
                # y lo metemos a nuestra nueva lista con append()
                ganador = izquierda.pop(0)
                lista_ordenada.append(ganador)
            else:
                # Gana el de la derecha. Lo sacamos y lo metemos
                ganador = derecha.pop(0)
                lista_ordenada.append(ganador)
                
        # 4. Cuando una fila se vacía, metemos a todos los que sobraron en la otra
        for auto in izquierda:
            lista_ordenada.append(auto)
            
        for auto in derecha:
            lista_ordenada.append(auto)
            
        # 5. Por último, actualizamos nuestra lista original con los autos ya ordenados
        for j in range(len(lista_ordenada)):
            lista[o + j] = lista_ordenada[j]
    def ordenar_autos_anio(lista, o, i):
        tamanio = i - o
        
        # Criterio de paro 1: Un solo elemento
        if tamanio <= 1:
            return
            
        # Criterio de paro 2: Exactamente dos elementos
        if tamanio == 2:
            if lista[o + 1] < lista[o]:
                # El swap de Python para intercambiarlos
                lista[o], lista[o + 1] = lista[o + 1], lista[o]
            return
        # 1. Encontrar el punto medio (usamos // para que dé un número entero)
        mitad = (o + i) // 2
        
        # 2. Llamar a la recursividad para la mitad izquierda y la mitad derecha
        Automovil.ordenar_autos_anio(lista, o, mitad)
        Automovil.ordenar_autos_anio(lista, mitad, i)
        
        # 3. Mandar a llamar a nuestro "jefe final": la función que junta las mitades
        Automovil.fusionar(lista, o, mitad, i)
