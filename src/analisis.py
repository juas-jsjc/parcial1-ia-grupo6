import csv
import statistics

with open("grupo_06.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    registros = list(lector)
    
    print("Primeras 5 filas:")
    
    for fila in registros[:5]:
        print(fila)
        
    print("\nTotal de registros:", len(registros))

with open("grupo_06.csv", "r") as archivo:
    lector = csv.DictReader(archivo)

    consumos = []

    for fila in lector:
        # Ignorar valores faltantes
        if fila["consumo_m3"] != "":
            consumo = float(fila["consumo_m3"])

            # Ignorar el valor atípico de 110000
            if consumo != 110000:
                consumos.append(consumo)
    
# Calcular estadísticas
media = statistics.mean(consumos)
mediana = statistics.median(consumos)
desviacion = statistics.stdev(consumos)
minimo = min(consumos)
maximo = max(consumos)

# Mostrar resultados
print("ANÁLISIS ESTADÍSTICO")
print("--------------------")
print(f"Registros analizados: {len(consumos)}")
print(f"Media: {media:.2f} m³")
print(f"Mediana: {mediana:.2f} m³")
print(f"Desviación estándar: {desviacion:.2f} m³")
print(f"Mínimo: {minimo:.2f} m³")
print(f"Máximo: {maximo:.2f} m³")

