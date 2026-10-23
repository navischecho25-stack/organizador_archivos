import os
import shutil

# 1. Definimos la ruta de la carpeta objetivo (la carpeta actual)
directorio_objetivo = "."

# 2. Diccionario que define qué extensión va a qué carpeta
extensiones_carpetas = {
    ".csv": "Reportes_CSV",
    ".xlsx": "Reportes_Excel",
    ".pdf": "Documentos_PDF",
    ".txt": "Archivos_Texto",
    ".png": "Imagenes",
    ".jpg": "Imagenes"
}

def crear_archivos_prueba():
    """Crea archivos de prueba si la carpeta está vacía para ver la magia en acción."""
    archivos_prueba = ["reporte_ventas.txt", "datos_cliente.csv", "factura_1.pdf"]
    print("🛠️ Creando archivos de prueba automáticos...")
    for archivo in archivos_prueba:
        if not os.path.exists(archivo):
            with open(archivo, "w") as f:
                f.write("Este es un archivo de prueba automático.")

def organizar_archivos():
    # Primero asegurarnos de que haya archivos para organizar
    crear_archivos_prueba()
    
    print("\nIniciando la organización de archivos...\n")
    
    # Listamos todos los archivos en el directorio
    archivos = os.listdir(directorio_objetivo)
    
    movidos = 0
    
    for archivo in archivos:
        # Omitimos carpetas y al propio script para no moverlos
        if os.path.isdir(archivo) or archivo == "organizador.py":
            continue
            
        # Obtenemos la extensión del archivo en minúsculas
        nombre, extension = os.path.splitext(archivo)
        
        if extension in extensiones_carpetas:
            nombre_carpeta = extensiones_carpetas[extension]
            
            # Creamos la carpeta destino si no existe
            if not os.path.exists(nombre_carpeta):
                os.makedirs(nombre_carpeta)
                print(f"📁 Carpeta creada: {nombre_carpeta}")
                
            # Rutas de origen y destino
            origen = archivo
            destino = os.path.join(nombre_carpeta, archivo)
            
            # Movemos el archivo
            shutil.move(origen, destino)
            print(f"-> Movido: {archivo}  ==>  {nombre_carpeta}/")
            movidos += 1

    print(f"\n✨ ¡Proceso finalizado! Se organizaron {movidos} archivos con éxito.")

if __name__ == "__main__":
    organizar_archivos()