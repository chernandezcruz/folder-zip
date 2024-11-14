import os
import subprocess
import platform
from datetime import datetime

# Verifica si el sistema operativo es Linux
if platform.system() != "Linux":
    print("Este script solo puede ejecutarse en sistemas operativos Linux.")
    exit()

# Configuración
zip_password = ""  # Contraseña para los archivos ZIP
directory = ""  # Ruta de la carpeta principal

# Verifica que la ruta exista y sea una carpeta
if not os.path.isdir(directory):
    print(f"La ruta especificada '{directory}' no existe o no es una carpeta.")
else:
    # Obtiene todas las carpetas dentro del directorio
    subfolders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]

    for subfolder_name in subfolders:
        # Genera el nombre del archivo ZIP: incluye el nombre de la subcarpeta y la fecha actual
        current_date = datetime.now().strftime("%Y-%m-%d")
        zip_filename = f"{subfolder_name}_backup_{current_date}.zip"
        subfolder_path = os.path.join(directory, subfolder_name)

        # Crea el archivo ZIP protegido con contraseña
        subprocess.run(["zip", "-P", zip_password, "-r", zip_filename, subfolder_path])
        print(f"Archivo ZIP creado: {zip_filename}")
