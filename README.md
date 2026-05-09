# Analisis de Resultados Deportivos

## Integrante
Martin Sterli

## Escenario elegido
Escenario D - Estadisticas de Resultados Deportivos

## Descripcion del proyecto
Este proyecto analiza resultados de partidos de futbol utilizando Python.
El programa lee un archivo CSV con distintos partidos y calcula los puntos
obtenidos por cada equipo segun los resultados. Luego genera una tabla de
posiciones y un grafico comparativo de rendimiento entre equipos.

## Dataset utilizado
Archivo: datos/partidos.csv
Datos simulados de partidos entre equipos argentinos (River, Boca, Racing,
Independiente, San Lorenzo). Contiene columnas: Equipo_Local, Equipo_Visitante,
Goles_Local, Goles_Visitante.

## Estructura del proyecto
- datos/ : carpeta donde se encuentra el archivo CSV con los partidos
- scripts/ : carpeta donde se encuentra el programa desarrollado en Python
- resultados/ : carpeta destinada a guardar resultados generados por el script

## Instrucciones para ejecutar el script
Desde la carpeta scripts ejecutar:
python analisis_datos.py
