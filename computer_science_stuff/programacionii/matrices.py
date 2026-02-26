"""
Multiplicación de Matrices — A, B, C, D
El usuario escribe la expresión primero (ej: A*B, A*(B*C), (A*B)*C*D)
y luego el programa pide las dimensiones y valores de cada matriz necesaria.
"""

import re

# ─────────────────────────────────────────────
#  UTILIDADES DE ENTRADA
# ─────────────────────────────────────────────

def pedir_entero(mensaje, minimo=1):
    while True:
        try:
            val = int(input(mensaje))
            if val >= minimo:
                return val
            print(f"  ⚠  El valor debe ser >= {minimo}.")
        except ValueError:
            print("  ⚠  Ingresa un número entero válido.")


def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  ⚠  Ingresa un número válido.")


def pedir_opcion(mensaje, opciones_validas):
    validas = [o.lower() for o in opciones_validas]
    while True:
        resp = input(mensaje).strip().lower()
        if resp in validas:
            return resp
        print(f"  ⚠  Opciones válidas: {', '.join(opciones_validas)}")


# ─────────────────────────────────────────────
#  MATRICES
# ─────────────────────────────────────────────

def ingresar_matriz(nombre, filas, columnas):
    print(f"\n  Ingresa los valores de la Matriz {nombre} ({filas}x{columnas}):")
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            v = pedir_float(f"    {nombre}[{i+1}][{j+1}]: ")
            fila.append(v)
        matriz.append(fila)
    return matriz


def multiplicar_dos(A, B, na, nb):
    filas_A, cols_A = len(A), len(A[0])
    filas_B, cols_B = len(B), len(B[0])
    if cols_A != filas_B:
        raise ValueError(
            f"  ✖  No compatible: {na}({filas_A}x{cols_A}) x {nb}({filas_B}x{cols_B})\n"
            f"     Columnas de {na} ({cols_A}) deben ser iguales a filas de {nb} ({filas_B})."
        )
    res = [[sum(A[i][k] * B[k][j] for k in range(cols_A))
            for j in range(cols_B)]
           for i in range(filas_A)]
    return res


def imprimir_matriz(matriz, titulo=""):
    if titulo:
        print(f"\n  +-- {titulo}")
    ancho = max(len(f"{v:.2f}") for fila in matriz for v in fila)
    for fila in matriz:
        print("  |  [ " + "  ".join(f"{v:{ancho}.2f}" for v in fila) + " ]")


def dims(m):
    return f"{len(m)}x{len(m[0])}"


# ─────────────────────────────────────────────
#  PARSER DE EXPRESIÓN
# ─────────────────────────────────────────────

def extraer_letras(expresion):
    """Devuelve lista de letras únicas usadas en la expresión, en orden de aparición."""
    vistas = []
    for c in expresion:
        if c in "ABCD" and c not in vistas:
            vistas.append(c)
    return vistas


def tokenizar(expr):
    """Convierte la expresión a lista de tokens: letras, *, (, )"""
    tokens = []
    for c in expr:
        if c in "ABCD*()" :
            tokens.append(c)
        elif c not in " ":
            raise ValueError(f"Carácter no válido: '{c}'")
    return tokens


def evaluar_expr(tokens, pos, matrices):
    """
    Parser recursivo descendente para expresiones con * y paréntesis.
    Gramática:
      expr   := term  (* term)*
      term   := LETRA | '(' expr ')'
    Retorna (matriz_resultado, nombre_str, nueva_posicion)
    """
    resultado, nombre, pos = parsear_expr(tokens, pos, matrices)
    return resultado, nombre, pos


def parsear_expr(tokens, pos, matrices):
    izq, nombre_izq, pos = parsear_term(tokens, pos, matrices)

    while pos < len(tokens) and tokens[pos] == '*':
        pos += 1  # consumir '*'
        der, nombre_der, pos = parsear_term(tokens, pos, matrices)
        nombre_nuevo = f"({nombre_izq}*{nombre_der})"
        print(f"\n  >> Calculando {nombre_izq} x {nombre_der} ...", end=" ")
        izq = multiplicar_dos(izq, der, nombre_izq, nombre_der)
        print(f"OK -> {dims(izq)}")
        nombre_izq = nombre_nuevo

    return izq, nombre_izq, pos


def parsear_term(tokens, pos, matrices):
    if pos >= len(tokens):
        raise ValueError("Expresión incompleta.")

    tok = tokens[pos]

    if tok == '(':
        pos += 1  # consumir '('
        res, nombre, pos = parsear_expr(tokens, pos, matrices)
        if pos >= len(tokens) or tokens[pos] != ')':
            raise ValueError("Falta ')' en la expresión.")
        pos += 1  # consumir ')'
        return res, nombre, pos

    elif tok in "ABCD":
        if tok not in matrices:
            raise ValueError(f"La matriz '{tok}' no fue definida.")
        pos += 1
        return matrices[tok], tok, pos

    else:
        raise ValueError(f"Token inesperado: '{tok}'")


# ─────────────────────────────────────────────
#  MENÚ DE EXPRESIÓN
# ─────────────────────────────────────────────

EJEMPLOS = [
    "A*B",
    "B*A",
    "A*(B*C)",
    "(A*B)*C",
    "A*B*C*D",
    "(A*B)*(C*D)",
    "A*(B*(C*D))",
]

def mostrar_menu_expresion():
    print("\n" + "="*52)
    print("   MULTIPLICACION DE MATRICES")
    print("="*52)
    print("  Letras disponibles: A  B  C  D")
    print("  Operador: *    Agrupacion: ( )")
    print()
    print("  Ejemplos de expresiones:")
    for i, ej in enumerate(EJEMPLOS, 1):
        print(f"    {i}. {ej}")
    print()
    print("  Escribe un numero para usar un ejemplo")
    print("  o escribe tu propia expresion.")
    print("-"*52)


def pedir_expresion():
    while True:
        mostrar_menu_expresion()
        raw = input("  Tu expresion: ").strip()

        # Si escribió un número, usar el ejemplo
        if raw.isdigit():
            idx = int(raw) - 1
            if 0 <= idx < len(EJEMPLOS):
                expr = EJEMPLOS[idx]
                print(f"  --> Usando: {expr}")
            else:
                print(f"  ⚠  Número fuera de rango. Elige del 1 al {len(EJEMPLOS)}.")
                continue
        else:
            expr = raw.upper().replace(" ", "")

        # Validar caracteres
        if not re.fullmatch(r'[ABCD*()\s]+', expr.replace(" ", "")):
            print("  ⚠  Solo se permiten letras A-D, *, (, )")
            continue

        # Verificar letras válidas
        letras = extraer_letras(expr)
        if len(letras) == 0:
            print("  ⚠  La expresion debe contener al menos una letra (A, B, C, D).")
            continue
        if len(letras) == 1:
            print("  ⚠  Necesitas al menos 2 matrices diferentes para multiplicar.")
            continue

        return expr, letras


# ─────────────────────────────────────────────
#  CONFIGURAR MATRICES PEDIDAS
# ─────────────────────────────────────────────

def configurar_matrices(letras):
    """Pide dimensiones y valores solo de las matrices que aparecen en la expresión."""
    matrices = {}
    print(f"\n  La expresion usa las matrices: {', '.join(letras)}")
    print("  Ahora ingresa las dimensiones y valores de cada una.\n")

    for letra in letras:
        while True:
            print(f"  {'─'*44}")
            print(f"  Matriz {letra}")
            print(f"  {'─'*44}")
            filas = pedir_entero(f"  Filas    de {letra}: ")
            cols  = pedir_entero(f"  Columnas de {letra}: ")
            print(f"\n  Matriz {letra} sera de {filas}x{cols}.")
            confirmar = pedir_opcion(
                "  Es correcto? (s/n): ", ["s", "n"]
            )
            if confirmar == "s":
                break
            print(f"\n  Ok, vuelve a ingresar las dimensiones de {letra}.")

        matrices[letra] = ingresar_matriz(letra, filas, cols)

    return matrices


# ─────────────────────────────────────────────
#  PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────

def main():
    while True:
        # 1. El usuario escribe la expresión primero
        expr, letras = pedir_expresion()

        # 2. Pedir dimensiones y valores de las matrices necesarias
        matrices = configurar_matrices(letras)

        # 3. Mostrar matrices ingresadas
        print(f"\n  {'='*48}")
        print("  Matrices ingresadas:")
        for letra in letras:
            imprimir_matriz(matrices[letra], f"Matriz {letra}  {dims(matrices[letra])}")

        # 4. Evaluar la expresión
        print(f"\n  {'='*48}")
        print(f"  Evaluando: {expr}")
        try:
            tokens = tokenizar(expr)
            resultado, nombre_final, _ = parsear_expr(tokens, 0, matrices)

            # 5. Mostrar resultado
            print(f"\n  {'='*48}")
            imprimir_matriz(resultado,
                f"Resultado  {expr}  =  {dims(resultado)}")
            print(f"  {'='*48}")

        except ValueError as e:
            print(f"\n{e}")
            print("  Revisa que las dimensiones sean compatibles con la expresion.")

        # 6. ¿Qué sigue?
        print()
        op = pedir_opcion(
            "  Que deseas hacer?\n"
            "    [r] Nueva operacion (nueva expresion y matrices)\n"
            "    [e] Cambiar expresion (reusar mismas matrices)\n"
            "    [s] Salir\n"
            "  Opcion: ",
            ["r", "e", "s"]
        )

        if op == "s":
            print("\n  Hasta luego!\n")
            break

        elif op == "e":
            # Reusar matrices, cambiar expresion
            letras_actuales = list(matrices.keys())
            print(f"\n  Matrices disponibles: {', '.join(letras_actuales)}")
            for l in letras_actuales:
                print(f"    {l}: {dims(matrices[l])}")

            while True:
                nueva = input("\n  Nueva expresion: ").strip().upper().replace(" ","")
                letras_nuevas = extraer_letras(nueva)
                faltantes = [l for l in letras_nuevas if l not in matrices]
                if faltantes:
                    print(f"  ⚠  Matrices no cargadas: {', '.join(faltantes)}")
                    print(f"     Solo puedes usar: {', '.join(letras_actuales)}")
                    continue
                try:
                    tokens = tokenizar(nueva)
                    resultado, nombre_final, _ = parsear_expr(tokens, 0, matrices)
                    print(f"\n  {'='*48}")
                    imprimir_matriz(resultado,
                        f"Resultado  {nueva}  =  {dims(resultado)}")
                    print(f"  {'='*48}")
                except ValueError as e:
                    print(f"\n{e}")

                otra_expr = pedir_opcion(
                    "\n  Otra expresion con las mismas matrices? (s/n): ", ["s","n"]
                )
                if otra_expr == "n":
                    break
        # Si op == 'r', el while principal reinicia todo


if __name__ == "__main__":
    main()