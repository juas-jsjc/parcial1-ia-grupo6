import csv
with open("grupo_06.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    registros = list(lector)
    
    print("Primeras 5 filas:")
    
    for fila in registros[:5]:
        print(fila)
        
    print("\nTotal de registros:", len(registros))