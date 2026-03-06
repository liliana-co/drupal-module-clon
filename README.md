# Drupal Module Cloner

Este proyecto contiene un script en Python para clonar módulos de Drupal, renombrando archivos y modificando el contenido interno para adaptarlo a un nuevo nombre de módulo.

## ¿Qué hace el script?
- Copia un módulo Drupal existente a una nueva carpeta con el nombre que elijas.
- Renombra todos los archivos relevantes que contienen el nombre del módulo original.
- Reemplaza todas las ocurrencias del nombre del módulo original por el nuevo nombre dentro de los archivos (`php`, `yml`, `module`, `theme`, `install`).

## Uso
1. Ejecuta el script `main.py`.
2. Ingresa la ruta del módulo original que deseas clonar cuando se te solicite.
3. Ingresa el nuevo nombre para el módulo clonado.

El script creará una copia del módulo en la misma carpeta, con el nuevo nombre, y actualizará los nombres de archivos y referencias internas.

## Requisitos
- Python 3.x

## Ejemplo de ejecución
```
$ python main.py
entre la ruta origen del modulo a clonar: C:\ruta\al\modulo_original
escriba el nuevo nombre del modulo: modulo_nuevo
```

## Notas
- Asegúrate de tener permisos de escritura en la carpeta destino.
- Haz una copia de seguridad antes de usar el script en módulos importantes.

---

Autor: MariaLee
Fecha: marzo 2023
