import tkinter as tk
from tkinter import ttk
import random

def get_num_data():
    num_data = entry_num_data.get()
    try:
        num_data = int(num_data)
        if num_data > 0:
            enter_data_window(num_data)
            root.withdraw()  # Ocultar la ventana principal temporalmente
        else:
            label_error.config(text="Por favor, ingresa un número válido.")
    except ValueError:
        label_error.config(text="Por favor, ingresa un número válido.")

def enter_data_window(num_data):
    data_window = tk.Toplevel(root)
    data_window.title("Ingresar Datos")

    def add_data():
        nonlocal num_data  # Acceder a la variable num_data del ámbito externo
        new_data = entry_new_data.get()
        if new_data:
            data_list.append(new_data)
            entry_new_data.delete(0, tk.END)
            num_data -= 1
            if num_data == 0:
                data_window.destroy()
                show_random_data()
            else:
                entry_new_data.focus()

    for i in range(num_data):
        label = tk.Label(data_window, text=f"Dato {i + 1}:")
        label.grid(row=i, column=0, sticky="w", padx=10, pady=5)
        entry_new_data = tk.Entry(data_window)
        entry_new_data.grid(row=i, column=1, padx=10, pady=5)
        entry_new_data.focus()

    submit_button = tk.Button(data_window, text="Siguiente", command=add_data)
    submit_button.grid(row=num_data, columnspan=2, pady=10)

def show_random_data():
    random.shuffle(data_list)
    result_window = tk.Toplevel(root)
    result_window.title("Datos Ingresados Aleatoriamente")

    result_label = tk.Label(result_window, text=", ".join(data_list))
    result_label.pack(padx=10, pady=10)

root = tk.Tk()
root.title("Ingresar Número de Datos")

style = ttk.Style()
style.configure("TButton", padding=5, relief="flat")

label_instruction = tk.Label(root, text="Ingrese el número de datos:", font=("Arial", 12))
label_instruction.pack(pady=10)

entry_num_data = tk.Entry(root, font=("Arial", 12))
entry_num_data.pack()

submit_button = tk.Button(root, text="Continuar", command=get_num_data, font=("Arial", 12), relief="flat")
submit_button.pack(pady=10)

label_error = tk.Label(root, text="", fg="red")
label_error.pack()

data_list = []

root.mainloop()
