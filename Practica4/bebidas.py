import sqlite3

# Crear la base de datos y la tabla
def crear_base_datos():
    def crear_tabla():
        conn = sqlite3.connect('almacen_bebidas.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS bebidas
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nombre TEXT,
                 clasificacion TEXT,
                 marca TEXT,
                 precio REAL)''')
        conn.commit()
        conn.close()

# Insertar una nueva bebida
def alta_bebida(id, nombre, clasificacion, marca, precio):
    conn = sqlite3.connect('almacen_bebida.db')
    c = conn.cursor()

    # Insertar los valores en la tabla
    c.execute("INSERT INTO bebidas VALUES (?, ?, ?, ?, ?)", (id, nombre, clasificacion, marca, precio))

    conn.commit()
    conn.close()

# Eliminar una bebida por su ID
def baja_bebida(id):
    conn = sqlite3.connect('almacen_bebidaa.db')
    c = conn.cursor()

    # Eliminar la bebida de la tabla
    c.execute("DELETE FROM bebidas WHERE id=?", (id,))

    conn.commit()
    conn.close()

# Actualizar los datos de una bebida
def actualizar_bebida(id, nombre, clasificacion, marca, precio):
    conn = sqlite3.connect('almacen_bebida.db')
    c = conn.cursor()

    # Actualizar los valores de la bebida en la tabla
    c.execute("UPDATE bebidas SET nombre=?, clasificacion=?, marca=?, precio=? WHERE id=?",
              (nombre, clasificacion, marca, precio, id))

    conn.commit()
    conn.close()

# Mostrar todas las bebidas
def mostrar_bebidas():
    conn = sqlite3.connect('almacen_bebida.db')
    c = conn.cursor()

    # Obtener todas las bebidas de la tabla
    c.execute("SELECT * FROM bebidas")
    bebidas = c.fetchall()

    # Mostrar las bebidas
    print("---- Almacén de Bebidas ----")
    print("ID\t\tNombre\t\tClasificación\tMarca\t\tPrecio")
    print("----------------------------------------------")
    for bebida in bebidas:
        id = bebida[0]
        nombre = bebida[1]
        clasificacion = bebida[2]
        marca = bebida[3]
        precio = bebida[4]
        print(f"{id}\t\t{nombre}\t\t{clasificacion}\t{marca}\t\t${precio:.2f}")
    print("----------------------------------------------")

    conn.close()

# Calcular el precio promedio de las bebidas
def calcular_precio_promedio():
    conn = sqlite3.connect('almacen_bebida.db')
    c = conn.cursor()

    # Calcular el precio promedio
    c.execute("SELECT AVG(precio) FROM bebidas")
    precio_promedio = c.fetchone()[0]

    conn.close()

    return precio_promedio

# Calcular la cantidad de bebidas de una marca
def calcular_cantidad_por_marca(marca):
    conn = sqlite3.connect('almacen_bebida.db')
    c = conn.cursor()

    # Contar la cantidad de bebidas de la marca especificada
    c.execute("SELECT COUNT(*) FROM bebidas WHERE marca=?", (marca,))
    cantidad = c.fetchone()[0]

    conn.close()

    return cantidad

# Calcular la cantidad de bebidas por clasificación
def calcular_cantidad_por_clasificacion(clasificacion):
    conn = sqlite3.connect('almacen_bebida.db')
    c = conn.cursor()

    # Contar la cantidad de bebidas de la clasificación especificada
    c.execute("SELECT COUNT(*) FROM bebidas WHERE clasificacion=?", (clasificacion,))
    cantidad = c.fetchone()[0]

    conn.close()

    return cantidad

# Función para mostrar el menú y recibir la opción del usuario
def mostrar_menu():
    print("---------- Almacén de Bebidas ----------")
    print("1. Mostrar todas las bebidas")
    print("2. Agregar una nueva bebida")
    print("3. Actualizar datos de una bebida")
    print("4. Eliminar una bebida")
    print("5. Calcular el precio promedio de las bebidas")
    print("6. Calcular cantidad de bebidas de una marca")
    print("7. Calcular cantidad de bebidas por clasificación")
    print("0. Salir")
    print("----------------------------------------")
    opcion = input("Ingrese la opción deseada: ")
    print("----------------------------------------")
    return opcion

# Función principal
def main():
    crear_base_datos()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            mostrar_bebidas()
        elif opcion == "2":
            nombre = input("Nombre de la bebida: ")
            clasificacion = input("Clasificación de la bebida: ")
            marca = input("Marca de la bebida: ")
            precio = float(input("Precio de la bebida: $"))
            alta_bebida(None, nombre, clasificacion, marca, precio)
            print("¡Bebida agregada correctamente!")
        elif opcion == "3":
            id = int(input("ID de la bebida a actualizar: "))
            nombre = input("Nuevo nombre de la bebida: ")
            clasificacion = input("Nueva clasificación de la bebida: ")
            marca = input("Nueva marca de la bebida: ")
            precio = float(input("Nuevo precio de la bebida: $"))
            actualizar_bebida(id, nombre, clasificacion, marca, precio)
            print("¡Bebida actualizada correctamente!")
        elif opcion == "4":
            id = int(input("ID de la bebida a eliminar: "))
            baja_bebida(id)
            print("¡Bebida eliminada correctamente!")
        elif opcion == "5":
            precio_promedio = calcular_precio_promedio()
            print("El precio promedio de las bebidas es: ${:.2f}".format(precio_promedio))
        elif opcion == "6":
            marca = input("Ingrese la marca de las bebidas: ")
            cantidad = calcular_cantidad_por_marca(marca)
            print("La cantidad de bebidas de la marca {} es: {}".format(marca, cantidad))
        elif opcion == "7":
            clasificacion = input("Ingrese la clasificación de las bebidas: ")
            cantidad = calcular_cantidad_por_clasificacion(clasificacion)
            print("La cantidad de bebidas de la clasificación {} es: {}".format(clasificacion, cantidad))
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
