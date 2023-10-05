import tkinter as tk
import random

def fisher_yates_shuffle(numbers):
    shuffled_numbers = numbers.copy()
    n = len(shuffled_numbers)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        shuffled_numbers[i], shuffled_numbers[j] = shuffled_numbers[j], shuffled_numbers[i]
    return shuffled_numbers

def randomize_numbers():
    num_to_randomize = int(entry_num_to_randomize.get())
    numbers = entry_numbers.get().split(',')
    
    # Asegurarse de que haya suficientes números para aleatorizar
    if len(numbers) < num_to_randomize:
        result_label.config(text="No hay suficientes números para aleatorizar.")
        return
    
    # Aleatorizar los números
    randomized_numbers = fisher_yates_shuffle(numbers)
    
    # Mostrar los números aleatorizados en fila
    result_label.config(text="Números aleatorizados:\n" + ', '.join(randomized_numbers[:num_to_randomize]))

# Crear la ventana
window = tk.Tk()
window.title("Aleatorizar Números")

# Crear etiquetas y campos de entrada
num_to_randomize_label = tk.Label(window, text="Cantidad de números a aleatorizar:")
entry_num_to_randomize = tk.Entry(window)

numbers_label = tk.Label(window, text="Lista de números (separados por coma):")
entry_numbers = tk.Entry(window)

result_label = tk.Label(window, text="")

# Crear botón para aleatorizar los números
randomize_button = tk.Button(window, text="Aleatorizar Números", command=randomize_numbers)

# Colocar los elementos en la ventana
num_to_randomize_label.pack()
entry_num_to_randomize.pack()
numbers_label.pack()
entry_numbers.pack()
randomize_button.pack()
result_label.pack()

# Iniciar la ventana
window.mainloop()
