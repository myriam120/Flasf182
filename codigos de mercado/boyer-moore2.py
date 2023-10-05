import tkinter as tk
from collections import Counter

def find_majority_number():
    input_text = entry_numbers.get()
    numbers = [int(num) for num in input_text.split(',')]
    
    # Contar las ocurrencias de cada número
    counts = Counter(numbers)
    
    # Encontrar el número con la mayor cantidad de ocurrencias
    majority_number, majority_count = counts.most_common(1)[0]
    
    result_label.config(text=f"Número mayoritario: {majority_number} (aparece {majority_count} veces)")

# Crear la ventana
window = tk.Tk()
window.title("Encontrar el Número Mayoritario")

# Crear etiqueta y campo de entrada
numbers_label = tk.Label(window, text="Lista de números (separados por coma):")
entry_numbers = tk.Entry(window)

result_label = tk.Label(window, text="")

# Crear botón para encontrar el número mayoritario
find_button = tk.Button(window, text="Encontrar Número Mayoritario", command=find_majority_number)

# Colocar los elementos en la ventana
numbers_label.pack()
entry_numbers.pack()
find_button.pack()
result_label.pack()

# Iniciar la ventana
window.mainloop()
