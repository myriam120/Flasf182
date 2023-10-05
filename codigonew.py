import tkinter as tk
from random import randrange

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def shuffle(A):
    for i in range(len(A) - 1):
        j = randrange(i, len(A))
        swap(A, i, j)

def shuffle_and_display():
    num_entries = int(entry_num.get())
    data = []
    for i in range(num_entries):
        data.append(entry_data[i].get())
    
    shuffle(data)
    
    result_label.config(text=', '.join(data))

# Crear la ventana principal
root = tk.Tk()
root.title("Mezclador de Datos")

# Crear etiqueta y entrada para el número de datos
num_label = tk.Label(root, text="Número de datos:")
num_label.pack()
entry_num = tk.Entry(root)
entry_num.pack()

# Crear una lista para almacenar las entradas de datos
entry_data = []

# Función para agregar entradas de datos según el número ingresado
def add_data_entries():
    num_entries = int(entry_num.get())
    for i in range(num_entries):
        data_label = tk.Label(root, text=f"Dato {i + 1}:")
        data_label.pack()
        data_entry = tk.Entry(root)
        data_entry.pack()
        entry_data.append(data_entry)

# Botón para agregar las entradas de datos
add_button = tk.Button(root, text="Agregar Datos", command=add_data_entries)
add_button.pack()
# Botón para realizar el shuffle y mostrar el resultado
shuffle_button = tk.Button(root, text="Mezclar y Mostrar", command=shuffle_and_display)
shuffle_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

