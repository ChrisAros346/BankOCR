import os

def leer_cartas(numero):
    numero_str = str(numero).zfill(9)

    # Define la representación de cada dígito en una matriz 3x3 con pipes y guiones largos:
    digitos = {
        '0': [' _ ',
              '| |',
              '|_|'],

        '1': ['   ',
              '  |',
              '  |'],

        '2': [' _ ',
              ' _|',
              '|_ '],

        '3': [' _ ',
              ' _|',
              ' _|'],

        '4': ['   ',
              '|_|',
              '  |'],

        '5': [' _ ',
              '|_ ',
              ' _|'],

        '6': [' _ ',
              '|_ ',
              '|_|'],

        '7': [' _ ',
              '  |',
              '  |'],

        '8': [' _ ',
              '|_|',
              '|_|'],

        '9': [' _ ',
              '|_|',
              '  |']
    }

    # Inicializa los renglones de impresión:
    lineas = [''] * 3

    # Construye el lienzo de impresión ( 3 renglones x 27 caracteres ):
    for d in numero_str:
        for i, linea in enumerate(digitos[d]):
            lineas[i] += linea + ''

    # Imprime las 3 líneas y establece el número de caracteres a 27:
    for linea in lineas:
        print(linea[:27])

    # Validar el número e imprimir si es válido o no
    if calcular_checksum(numero):
        print("OK")
    else:
        print("ERR")


# Función para leer números desde un archivo txt en la misma carpeta del programa:
def leer_archivo(archivo):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    archivo_path = os.path.join(script_dir, archivo)

    with open(archivo_path, 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            numero = int(linea.strip())
            leer_cartas(numero)

# Hacer la validación del número de cuenta:
def calcular_checksum(numero):
    numero_str = str(numero).zfill(9)
    suma = 0
    for i in range(9):
        suma += int(numero_str[i]) * (9 - i)
    return suma % 11 == 0

archivo_ejemplo = "numeros.txt"
leer_archivo(archivo_ejemplo)