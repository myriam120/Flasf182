import sqlite3
import tkinter as tk
from tkinter import messagebox

class Bebida:
    def __init__(self, id, nombre, clasificacion, marca, precio):
        self.id = id
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.marca = marca
        self.precio = precio

class AlmacenBebidas:
    def __init__(self):
        self.connection = sqlite3.connect("C:/Users/majo0/Documents/GitHub/Flas182/Practica4/AlmacenBebidas.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS bebidas (id INTEGER PRIMARY KEY, nombre TEXT, clasificacion TEXT, marca TEXT, precio REAL)")
        self.connection.commit()
 
    def __del__(self):
        self.connection.close()

    def agregar_bebida(self, bebida):
        self.cursor.execute("INSERT INTO bebidas VALUES (?, ?, ?, ?, ?)", (bebida.id, bebida.nombre, bebida.clasificacion, bebida.marca, bebida.precio))
        self.connection.commit()

    def eliminar_bebida(self, id):
        self.cursor.execute("DELETE FROM bebidas WHERE id = ?", (id,))
        self.connection.commit()

    def actualizar_bebida(self, id, nombre, clasificacion, marca, precio):
        self.cursor.execute("UPDATE bebidas SET nombre = ?, clasificacion = ?, marca = ?, precio = ? WHERE id = ?", (nombre, clasificacion, marca, precio, id))
        self.connection.commit()

    def mostrar_bebidas(self):
        self.cursor.execute("SELECT * FROM bebidas")
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Nombre: {row[1]}, Clasificación: {row[2]}, Marca: {row[3]}, Precio: {row[4]}")

    def calcular_precio_promedio(self):
        self.cursor.execute("SELECT AVG(precio) FROM bebidas")
        promedio = self.cursor.fetchone()[0]
        return promedio

    def contar_bebidas_marca(self, marca):
        self.cursor.execute("SELECT COUNT(*) FROM bebidas WHERE marca = ?", (marca,))
        cantidad = self.cursor.fetchone()[0]
        return cantidad

    def contar_bebidas_clasificacion(self, clasificacion):
        self.cursor.execute("SELECT COUNT(*) FROM bebidas WHERE clasificacion = ?", (clasificacion,))
        cantidad = self.cursor.fetchone()[0]
        return cantidad

class VentanaAlmacen:
    def __init__(self, root):
        self.root = root
        self.root.title("Almacén de Bebidas")
        self.almacen = AlmacenBebidas()
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Etiquetas y campos de texto para los atributos de la bebida
        tk.Label(self.frame, text="ID:").grid(row=0, column=0)
        self.id_entry = tk.Entry(self.frame)
        self.id_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Nombre:").grid(row=1, column=0)
        self.nombre_entry = tk.Entry(self.frame)
        self.nombre_entry.grid(row=1, column=1)
        
        tk.Label(self.frame, text="Clasificación:").grid(row=2, column=0)
        self.clasificacion_entry = tk.Entry(self.frame)
        self.clasificacion_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Marca:").grid(row=3, column=0)
        self.marca_entry = tk.Entry(self.frame)
        self.marca_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="Precio:").grid(row=4, column=0)
        self.precio_entry = tk.Entry(self.frame)
        self.precio_entry.grid(row=4, column=1)
        
        self.btn_agregar = tk.Button(self.frame, text="Agregar", command=self.agregar_bebida)
        self.btn_agregar.grid(row=0, column=2)

        self.btn_eliminar = tk.Button(self.frame, text="Eliminar", command=self.eliminar_bebida)
        self.btn_eliminar.grid(row=1, column=2)

        self.btn_actualizar = tk.Button(self.frame, text="Actualizar", command=self.actualizar_bebida)
        self.btn_actualizar.grid(row=2, column=2)

        self.btn_mostrar = tk.Button(self.frame, text="Mostrar Todas", command=self.mostrar_bebidas)
        self.btn_mostrar.grid(row=3, column=2)

        self.btn_calcular_promedio = tk.Button(self.frame, text="Calcular Precio Promedio", command=self.calcular_precio_promedio)
        self.btn_calcular_promedio.grid(row=4, column=2)

        self.btn_contar_marca = tk.Button(self.frame, text="Contar Bebidas por Marca", command=self.contar_bebidas_marca)
        self.btn_contar_marca.grid(row=5, column=2)

        self.btn_contar_clasificacion = tk.Button(self.frame, text="Contar Bebidas por Clasificación", command=self.contar_bebidas_clasificacion)
        self.btn_contar_clasificacion.grid(row=6, column=2)

        # Cuadro de texto para mostrar resultados
        self.result_text = tk.Text(self.frame, width=40, height=10)
        self.result_text.grid(row=5, column=0, columnspan=2, rowspan=2) 
       
    def agregar_bebida(self):
        try:
            id = int(self.id_entry.get())
            nombre = self.nombre_entry.get()
            clasificacion = self.clasificacion_entry.get()
            marca = self.marca_entry.get()
            precio = float(self.precio_entry.get())

            bebida = Bebida(id, nombre, clasificacion, marca, precio)
            self.almacen.agregar_bebida(bebida)

            messagebox.showinfo("Éxito", "Bebida agregada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar la bebida. Error: {str(e)}")

    def eliminar_bebida(self):
        try:
            id = int(self.id_entry.get())
            self.almacen.eliminar_bebida(id)
            messagebox.showinfo("Éxito", "Bebida eliminada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar la bebida. Error: {str(e)}")

    def actualizar_bebida(self):
        try:
            id = int(self.id_entry.get())
            nombre = self.nombre_entry.get()
            clasificacion = self.clasificacion_entry.get()
            marca = self.marca_entry.get()
            precio = float(self.precio_entry.get())

            self.almacen.actualizar_bebida(id, nombre, clasificacion, marca, precio)
            messagebox.showinfo("Éxito", "Bebida actualizada correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar la bebida. Error: {str(e)}")

    def mostrar_bebidas(self):
        self.result_text.delete("1.0", tk.END)
        bebidas = self.almacen.mostrar_bebidas()
        for bebida in bebidas:self.result_text.insert(tk.END, f"ID: {bebida[0]}, Nombre: {bebida[1]}, Clasificación: {bebida[2]}, Marca: {bebida[3]}, Precio: {bebida[4]}\n")

    def calcular_precio_promedio(self):
        promedio = self.almacen.calcular_precio_promedio()
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, f"Precio promedio de las bebidas: {promedio}")

    def contar_bebidas_marca(self):
        marca = self.marca_entry.get()
        cantidad = self.almacen.contar_bebidas_marca(marca)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, f"Cantidad de bebidas de la marca {marca}: {cantidad}")

    def contar_bebidas_clasificacion(self):
        clasificacion = self.clasificacion_entry.get()
        cantidad = self.almacen.contar_bebidas_clasificacion(clasificacion)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, f"Cantidad de bebidas de la clasificación {clasificacion}: {cantidad}")
        
root = tk.Tk()
app = VentanaAlmacen(root)
root.mainloop()