import csv
import matplotlib.pyplot as plt

with open("grupo_06.csv", "r") as archivo:
    lector = csv.DictReader(archivo)

    datos = []

    for fila in lector:

        if fila["consumo_m3"] == "":
            continue

        consumo = float(fila["consumo_m3"])

        # Excluir valor atípico
        if consumo == 110000:
            continue

        datos.append({
            "barrio": fila["barrio"],
            "consumo": consumo,
            "habitantes": int(fila["habitantes"]),
            "mes": fila["mes"]
        })


# ==========================
# GRÁFICO 1
# Distribución del consumo
# ==========================

consumos = []

for dato in datos:
    consumos.append(dato["consumo"])

plt.figure(figsize=(8, 5))

plt.hist(consumos, bins=6, edgecolor="black")

plt.title("Distribución del consumo de agua")
plt.xlabel("Consumo (m³)")
plt.ylabel("Cantidad de registros")

plt.savefig("distribucion_consumo.png")

plt.close()


# ==========================
# GRÁFICO 2
# Habitantes vs consumo
# ==========================

habitantes = []
consumos = []

for dato in datos:
    habitantes.append(dato["habitantes"])
    consumos.append(dato["consumo"])

plt.figure(figsize=(8, 5))

plt.scatter(habitantes, consumos)

plt.title("Relación entre habitantes y consumo")
plt.xlabel("Habitantes")
plt.ylabel("Consumo (m³)")

plt.savefig("habitantes_vs_consumo.png")

plt.close()


print("Análisis terminado.")
print("Se generaron los siguientes archivos:")
print("- distribucion_consumo.png")
print("- habitantes_vs_consumo.png")