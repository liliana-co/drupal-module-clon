# cli.py
import argparse
import sys
from .cloner import clone_module

def parse_args():
    parser = argparse.ArgumentParser(
        prog="module-cloner",
        description="Clona carpetas, archivos y su contenido reemplazando el nombre del módulo."
    )

    parser.add_argument(
        "source",
        help="Ruta de la carpeta fuente a clonar"
    )

    parser.add_argument(
        "--new-name",
        required=True,
        help="Nombre nuevo del módulo"
    )

    parser.add_argument(
        "--dest",
        help="Ruta destino donde se creará el clon"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Muestra detalle de cada archivo procesado"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    try:
        clone_module(
            source=args.source,
            new_name=args.new_name,
            dest=args.dest,
            verbose=args.verbose,
        )
        print(f"✅ Módulo {args.new_name} clonado exitosamente")

    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        sys.exit(1)