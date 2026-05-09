import csv

# Abrimos el archivo CSV con los datos de los partidos
archivo = open('../datos/partidos.csv', encoding='utf-8')
lector = csv.reader(archivo)
next(lector)  # Saltamos el encabezado

# Diccionario para guardar los puntos de cada equipo
puntos = {}

# Recorremos cada partido y calculamos los puntos
for fila in lector:
    local = fila[0]
    visitante = fila[1]
    goles_local = int(fila[2])
    goles_visitante = int(fila[3])

    # Inicializamos el equipo si no existe en el diccionario
    if local not in puntos:
        puntos[local] = 0
    if visitante not in puntos:
        puntos[visitante] = 0

    # Asignamos puntos segun el resultado
    if goles_local > goles_visitante:
        puntos[local] += 3
    elif goles_local < goles_visitante:
        puntos[visitante] += 3
    else:
        puntos[local] += 1
        puntos[visitante] += 1

archivo.close()

# Ordenamos la tabla de mayor a menor puntaje
tabla = sorted(puntos.items(), key=lambda x: x[1], reverse=True)

# Mostramos la tabla de posiciones
print("TABLA DE POSICIONES")
print("-" * 25)
for equipo, pts in tabla:
    print(f"{equipo}: {pts} puntos")

# Grafico de barras con asteriscos
print("\nGRAFICO DE PUNTOS")
print("-" * 25)
for equipo, pts in tabla:
    barra = "*" * pts
    print(f"{equipo:15} | {barra} ({pts})")

# Guardamos los resultados en un archivo de texto
resultado = open('../resultados/tabla_posiciones.txt', 'w')
resultado.write("TABLA DE POSICIONES\n")
resultado.write("-" * 25 + "\n")
for equipo, pts in tabla:
    resultado.write(f"{equipo}: {pts} puntos\n")
resultado.write("\nGRAFICO DE PUNTOS\n")
resultado.write("-" * 25 + "\n")
for equipo, pts in tabla:
    barra = "*" * pts
    resultado.write(f"{equipo:15} | {barra} ({pts})\n")
resultado.close()

print("\nResultados guardados en resultados/tabla_posiciones.txt")
