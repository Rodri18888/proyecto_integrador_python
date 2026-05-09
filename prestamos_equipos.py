#ESTRUCTURAS DE DATOS

equipos = {
    "equipo1" : {
        "nombre" : "Portatil1",
        "estado" : True,
        "prestamos" : []
    },
    "equipo2" : {
        "nombre" : "Portatil2",
        "estado" : True,
        "prestamos" : []
    },
    "equipo3" : {
        "nombre" : "Portatil3",
        "estado" : True,
        "prestamos" : []
    },
} 



#FUNCIONES

# Mostrar equipos

def mostrar_equipos():
    print("--Lista de equipos--")
    for equipo, info in equipos.items():
        print(f"Nombre: {info.get("nombre")}")
        if (info.get("estado")):
            print("Estado: Disponible")
        else:
            print("Estado: No disponible")
        print()    
    
        


# Registrar prestamo



# Devolver equipo



# Ver historial



# Agregar equipo



# Menu interactivo



