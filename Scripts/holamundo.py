# Script que crea un archivo de texto con un mensaje

nombre_archivo = "resultado.txt"

with open(nombre_archivo, "w") as archivo:
    archivo.write("¡Hola mundo desde GitHub Actions!\n")
    archivo.write("Este archivo fue generado automáticamente.\n")

print(f"Archivo '{nombre_archivo}' creado exitosamente.")