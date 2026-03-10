import random

# 1. DEFINICIÓN DE LA CLASE
class Automovil:
   
    # --- Atributos de Clase ---
    # Estos atributos son compartidos por TODOS los objetos de tipo Automovil.
    # range(2020, 2027) genera los años del 2020 al 2026.
    anio = range(2020, 2027) 
    
    # Un diccionario que relaciona marcas (llaves) con sus modelos (valores en una lista)
    diccionario = {
        "Toyota": ["Corola", "camry", "prius"],
        "Ford": ["Lobo", "f-150", "Explorador"],
        "Dodge": ["charger", "Durango", "ram"],
        "Honda": ["civic", "accord", "crv"],
        "Chevrolet": ["impala", "malibu", "silverado"],
        "Nissan": ["altima", "sentra", "rougue"],
        "Mazda": ["X7", "3", "5"]
    }

    # 2. CONSTRUCTOR (__init__)
    # Inicializa cada auto individual con valores por defecto si no se le pasan.
    def __init__(self, marca='honda', modelo='civic', anio='2021'):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    # 3. MÉTODO DE CLASE (Fábrica de autos)
    # Usa @classmethod para acceder a los atributos de la clase (Automovil.diccionario)
    # Su trabajo es generar un Auto completamente aleatorio y devolverlo.
    @classmethod
    def crea_auto(cls):
        # Elige una marca al azar de las llaves del diccionario
        marca = random.choice(list(Automovil.diccionario.keys()))
        # Elige un modelo al azar de la lista correspondiente a esa marca
        modelo = random.choice(Automovil.diccionario[marca])
        # Elige un año al azar del rango 2020-2026
        anio = random.choice(Automovil.anio)
        
        # Retorna un nuevo objeto Automovil instanciado con esos datos aleatorios
        return Automovil(marca, modelo, anio)

    # 4. MÉTODOS MÁGICOS (Dunder methods)
    # Define cómo se imprime el objeto en texto
    def __str__(self):
        return f"Soy un {self.marca} {self.modelo} del anio {self.anio}"

    # Define cómo funciona el símbolo "Menor que" (<) entre dos autos. (Sobrecarga de operadores)
    # Aquí le decimos a Python que un auto es "menor" que otro si su año es menor.
    def __lt__(self, other):
        return self.anio < other.anio

    # Define cómo funciona el símbolo "Mayor que" (>) entre dos autos.
    def __gt__(self, other):
        return self.anio > other.anio

    # ---------------------------------------------------------
    # 5. ALGORITMO DE ORDENAMIENTO: MERGE SORT (Mezcla)
    # ---------------------------------------------------------

    # MÉTODO FUSIONAR (La parte de "Vencerás")
    # Toma dos mitades de una lista que ya están ordenadas y las combina en una sola.
    @staticmethod
    def fusionar(lista, o, mitad, i):
        # 'o' es el origen (inicio), 'i' es el final.
        # Crea dos sublistas temporales: una izquierda y una derecha
        izquierda = lista[o:mitad]
        derecha = lista[mitad:i]
        
        lista_ordenada = [] # Aquí iremos guardando los ganadores
        
        # Mientras ambas listas tengan elementos, comparamos sus primeros elementos
        while len(izquierda) > 0 and len(derecha) > 0:
            
            # Aquí es donde entra en acción el método mágico __lt__ que definiste arriba
            if izquierda[0] < derecha[0]:
                # Si el de la izquierda es menor (más viejo), lo sacamos (.pop) y lo guardamos
                ganador = izquierda.pop(0)
                lista_ordenada.append(ganador)
            else:
                # Si el de la derecha es menor, ese es el ganador
                ganador = derecha.pop(0)
                lista_ordenada.append(ganador)
                
        # Si la lista derecha se vació primero, metemos todo lo que sobró de la izquierda
        for auto in izquierda:
            lista_ordenada.append(auto)
            
        # Si la lista izquierda se vació primero, metemos todo lo que sobró de la derecha
        for auto in derecha:
            lista_ordenada.append(auto)
            
        # Finalmente, reemplazamos los elementos desordenados de la lista original
        # por los elementos que acabamos de ordenar en esta pasada.
        for j in range(len(lista_ordenada)):
            lista[o + j] = lista_ordenada[j]

    # MÉTODO ORDENAR (La parte de "Divide")
    # Este método es RECURSIVO (se llama a sí mismo). Se encarga de partir la lista a la mitad.
    # Ojo: Técnicamente le faltaría el @staticmethod arriba para ser consistente, 
    # pero funciona porque lo llamas referenciando a Automovil.
    def ordenar_autos_anio(lista, o, i):
        tamanio = i - o # Calcula cuántos elementos estamos analizando
        
        # Caso base 1: Si la lista tiene 1 elemento o menos, ya está ordenada. Rompe la recursividad.
        if tamanio <= 1:
            return
     
        # Caso base 2: Si la lista tiene exactamente 2 elementos, simplemente los compara y los voltea si es necesario.
        if tamanio == 2:
            if lista[o + 1] < lista[o]:
                # Intercambio rápido de variables en Python (Swapping)
                lista[o], lista[o + 1] = lista[o + 1], lista[o]
            return

        # Si la lista tiene más de 2 elementos, calcula cuál es el índice de la mitad exacta
        mitad = (o + i) // 2
        
        # Se llama a sí mismo para partir y ordenar la mitad izquierda
        Automovil.ordenar_autos_anio(lista, o, mitad)
        
        # Se llama a sí mismo para partir y ordenar la mitad derecha
        Automovil.ordenar_autos_anio(lista, mitad, i)
        
        # Una vez que las dos mitades están ordenadas, llama a fusionar() para