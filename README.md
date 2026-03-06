# Drupal Module Cloner

Este proyecto contiene un módulo en Python para clonar módulos de Drupal, renombrando archivos y modificando el contenido interno para adaptarlo a un nuevo nombre de módulo. Ahora la funcionalidad está organizada como un paquete llamado `custom_cloner` y se utiliza a través de la interfaz de línea de comandos definida en `cli.py`.

## ¿Qué hace el módulo?
- Copia un módulo Drupal existente a una nueva carpeta con el nombre que elijas.
- Renombra todos los archivos relevantes que contienen el nombre del módulo original.
- Reemplaza todas las ocurrencias del nombre del módulo original por el nuevo nombre dentro de los archivos (`php`, `yml`, `module`, `theme`, `install`).

## Crear un ejecutable (opcional)
Puedes generar un ejecutable para Windows usando PyInstaller, lo que permite ejecutar el cloner directamente desde la terminal sin necesidad de Python instalado en el sistema destino.

1. Instala PyInstaller si no lo tienes:
	```
	pip install pyinstaller
	```
2. Desde la raíz del proyecto, ejecuta:
	```
	pyinstaller --onefile -m custom_cloner/__main__.py
	```
	Esto generará un ejecutable en la carpeta `dist/`.

3. Ahora puedes ejecutar el cloner desde la terminal:
	```
	dist\custom_cloner.exe <ruta_modulo_origen> --new-name <nuevo_nombre> [--dest <ruta_destino>] [--verbose]
	```

Ten en cuenta que el nombre del ejecutable puede variar según la configuración y el sistema operativo.

## Uso
Puedes ejecutar el clonado de módulos Drupal usando la interfaz de línea de comandos:

```
python -m custom_cloner <ruta_modulo_origen> --new-name <nuevo_nombre> [--dest <ruta_destino>] [--verbose]
```

Parámetros principales:
- `<ruta_modulo_origen>`: Ruta de la carpeta fuente a clonar.
- `--new-name`: Nombre nuevo del módulo (obligatorio).
- `--dest`: Ruta destino donde se creará el clon (opcional, por defecto en la misma carpeta que el origen).
- `--verbose` o `-v`: Muestra detalle de cada archivo procesado (opcional).

Ejemplo:
```
python -m custom_cloner.cli C:\ruta\al\modulo_original --new-name modulo_nuevo --dest C:\ruta\destino\
```

## Requisitos
- Python 3.x


## Notas
- Asegúrate de tener permisos de escritura en la carpeta destino.
- Haz una copia de seguridad antes de usar el script en módulos importantes.

---

Autor: MariaLee
Fecha: marzo 2026
