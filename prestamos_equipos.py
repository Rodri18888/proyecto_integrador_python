# prestamos_equipos.py
from datetime import date


# Clase que representa un equipo individual

class Equipo:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.disponible = True
        # Lista de tuplas inmutables (usuario, fecha)
        self.historial: list[tuple[str, str]] = []

    def prestar(self, usuario: str) -> None:
        """Registra el préstamo y cambia el estado del equipo."""
        if not self.disponible:
            raise ValueError(f"El equipo '{self.nombre}' ya está prestado.")
        fecha = str(date.today())
        self.historial.append((usuario, fecha)) # tupla inmutable
        self.disponible = False

    def devolver(self) -> None:
        """Marca el equipo como disponible."""
        if self.disponible:
            raise ValueError(f"El equipo '{self.nombre}' no está prestado actualmente.")
        self.disponible = True

    def estado_str(self) -> str:
        return "Disponible" if self.disponible else "Prestado"



# Clase principal que gestiona todo el inventario de préstamos

class SistemaPrestamos:
    def __init__(self):
        # Diccionario anidado: nombre_equipo -> objeto Equipo
        self.inventario: dict[str, Equipo] = {}

    def agregar_equipo(self, nombre: str) -> None:
        """Agrega un equipo nuevo al inventario."""
        nombre = nombre.strip()
        if nombre in self.inventario:
            print(f" El equipo '{nombre}' ya existe en el sistema.")
            return
        self.inventario[nombre] = Equipo(nombre)
        print(f" Equipo '{nombre}' registrado exitosamente.")

    def mostrar_equipos(self) -> None:
        """Muestra todos los equipos y su estado."""
        if not self.inventario:
            print(" No hay equipos registrados.")
            return
        print(f"\n {'Equipo':<25} {'Estado'}")
        print(" " + "-" * 35)
        for nombre, equipo in self.inventario.items():
            print(f" {nombre:<25} {equipo.estado_str()}")

    def registrar_prestamo(self) -> None:
        """Flujo completo para registrar un préstamo."""
        self.mostrar_equipos()
        nombre = input("\n Nombre del equipo a prestar: ").strip()
        if nombre not in self.inventario:
            print(f" Error: el equipo '{nombre}' no existe.")
            return
        usuario = input(" Nombre del usuario: ").strip()
        if not usuario:
            print(" Error: el nombre del usuario no puede estar vacío.")
            return
        try:
            self.inventario[nombre].prestar(usuario)
            print(f" Prestamo registrado: '{nombre}' -> {usuario}.")
        except ValueError as e:
            print(f" {e}")

    def devolver_equipo(self) -> None:
        """Flujo completo para registrar una devolución."""
        nombre = input(" Nombre del equipo a devolver: ").strip()
        if nombre not in self.inventario:
            print(f" Error: el equipo '{nombre}' no existe.")
            return
        try:
            self.inventario[nombre].devolver()
            print(f" Equipo '{nombre}' marcado como disponible.")
        except ValueError as e:
            print(f" {e}")

    def ver_historial(self) -> None:
        """Muestra el historial de préstamos de todos los equipos."""
        if not self.inventario:
            print(" No hay equipos registrados.")
            return
        for nombre, equipo in self.inventario.items():
            print(f"\n [ {nombre} ]")
            if not equipo.historial:
                print(" Sin préstamos registrados.")
            else:
                for usuario, fecha in equipo.historial:
                    print(f" - {usuario} ({fecha})")



# Función principal

def menu():
    sistema = SistemaPrestamos()

    # Datos de ejemplo
    for nombre in ["Laptop Dell 01", "Laptop HP 02", "Tablet Samsung 01"]:
        sistema.agregar_equipo(nombre)

    opciones = {
        "1": ("Ver equipos", sistema.mostrar_equipos),
        "2": ("Registrar préstamo", sistema.registrar_prestamo),
        "3": ("Devolver equipo", sistema.devolver_equipo),
        "4": ("Ver historial", sistema.ver_historial),
        "5": ("Agregar equipo", lambda: sistema.agregar_equipo(
            input(" Nombre del nuevo equipo: ").strip()
        )),
    }

    while True:
        print("\n" + "=" * 40)
        print(" SISTEMA DE PRESTAMOS DE EQUIPOS")
        print("=" * 40)
        for key, (label, _) in opciones.items():
            print(f" {key}. {label}")
        print("=" * 40)

        opcion = input(" Selecciona una opción: ").strip()

        if opcion not in opciones:
            print(" Opción no válida.")
            continue

        if opcion == "6":
            print(" Saliendo del sistema.")
            break

        _, accion = opciones[opcion]
        accion()



if __name__ == "__main__":
    menu()