# 📂 Organizador Automático de Archivos (`organizador.py`)

## 🎯 Descripción del Proyecto
Este script de automatización en Python (BPA - Business Process Automation) resuelve el problema del desorden en directorios de trabajo y descargas en entornos empresariales. El script clasifica y desplaza automáticamente archivos a subcarpetas específicas según su extensión (`.csv`, `.pdf`, `.txt`, `.xlsx`, etc.), optimizando el tiempo de búsqueda documental.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.14
* **Módulos Nativos:** `os` (gestión de rutas del sistema) y `shutil` (operaciones de movimiento de archivos)

## 🚀 Características
* **Clasificación Automática:** Detecta extensiones de archivo y crea carpetas de destino de forma dinámica.
* **Prueba Autónoma Incorporada:** Incluye una función que genera archivos temporales si la carpeta está vacía para validar el funcionamiento de inmediato.
* **Seguridad:** Omite carpetas del sistema y excluye al propio archivo ejecutable para evitar bucles.

## 💻 Instrucciones de Uso
1. Abre la terminal en el directorio del proyecto.
2. Ejecuta el script:
   ```bash
   python organizador.py