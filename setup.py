from setuptools import setup, find_packages
import sys

# ...existing code...
def do_setup():
    setup(
        name="clase1",
        version="0.1.0",
        packages=find_packages(),
        description="Ejemplo: imprimir valores y sus tipos con print() y type()",
    )

def demo_print_types():
    nombre: str = "Sergio"
    edad: int = 30
    altura: float = 1.75
    esAdmin: bool = False

    print(f"Nombre: {nombre} -> tipo: {type(nombre)}")
    print(f"Edad: {edad} -> tipo: {type(edad)}")
    print(f"Altura: {altura} m -> tipo: {type(altura)}")
    print(f"Es admin: {esAdmin} -> tipo: {type(esAdmin)}")
# ...existing code...

if __name__ == "__main__":
    # si se pasan argumentos (install, sdist, etc.) ejecutar setup()
    if len(sys.argv) > 1:
        do_setup()
    # si no, ejecutar el demo (python setup.py)
    else:
        demo_print_types()